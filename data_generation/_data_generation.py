import os
import json
import sys

current_directory = os.getcwd()
print(current_directory)
sys.path.insert(0, '/home/elias/Documents/10 Academy/WEEK 6/PrecisionRAG-AutomationSuite')

# project_root = os.path.dirname(os.path.abspath(__file__))
# os.chdir(project_root)

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from data_generation.retrive import retrieve_context

env_file_path = find_dotenv(raise_error_if_not_found=True)
load_dotenv(env_file_path)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def get_completion(messages, model="gpt-3.5-turbo", max_tokens=500, temperature=0, stop=None, seed=123, tools=None, logprobs=None, top_logprobs=None):
    params = {
        "messages": messages,
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stop": stop,
        "seed": seed,
        "logprobs": logprobs,
        "top_logprobs": top_logprobs,
    }
    if tools:
        params["tools"] = tools

    completion = client.chat.completions.create(**params)
    return completion

def file_reader(path):
    # current_script_directory = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory of the current script directory
   

# Get the grandparent directory (PrecisionRAG-AutomationSuite)
    # file_path = os.path.join(current_script_directory, path)

    fname = os.path.join( path)
    with open(fname, 'r') as f:
        return f.read()

def generate_test_data(prompt, context, num_test_output):
    API_RESPONSE = get_completion([
        {"role": "user", "content": prompt.replace("{context}", context).replace("{num_test_output}", num_test_output)}
    ], logprobs=True, top_logprobs=1)

    return API_RESPONSE.choices[0].message.content

def save_json(test_data):
    file_path = "test-dataset/test-data.json"
    json_object = json.loads(test_data)
    with open(file_path, 'w') as json_file:
        json.dump(json_object, json_file, indent=4)

    print(f"JSON data has been saved to {file_path}")

def main(num_test_output, inputText: str):
    context_message=context=retrieve_context(inputText)
  

# Get the parent directory of the current script directory
    # current_script_directory = os.path.dirname(os.path.realpath(__file__))
    # print(current_script_directory)

    # print(parent_directory)
    context = file_reader(os.path.join("prompts/context.txt"))
    prompt = file_reader(os.path.join("prompts/data-generation-prompt.txt"))
    test_data = generate_test_data(prompt, context, num_test_output)
    save_json(test_data)

    print("===========")
    print("Test Data")
    print("===========")
    print(test_data)

if __name__ == "__main__":
    user_input = str(input("inputText: "))
    main("5", user_input)  # n number of test data to generate
