
import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
sys.path.insert(0, '/home/elias/Documents/10 Academy/WEEK 6/PrecisionRAG-AutomationSuite')

# current_script_directory = os.path.dirname(os.path.realpath(__file__))
# print(current_script_directory)
# # # Get the parent directory of the current script directory
# # parent_directory = os.path.dirname(current_script_directory)

# # # Get the grandparent directory (PrecisionRAG-AutomationSuite)
# # grandparent_directory = os.path.dirname(parent_directory)
# # print(grandparent_directory)
# # # Add the grandparent directory to sys.path
# # sys.path.insert(0, grandparent_directory)

from data_generation._data_generation import main as generate_prompt_data, file_reader
from data_generation._evaluation import evaluate
from data_generation.retrive import retrieve_context
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText (BaseModel):
    inputText: str

@app.post("/apeg")
async def apeg(inputText: InputText):
    # Generate prompt data
    generate_prompt_data("5", inputText.inputText)

    # Read the generated prompts
    script_dir = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.dirname(script_dir)
    # file_path = os.path.join(base_dir, "test-dataset/test-data.json")
    current_script_directory = os.path.dirname(os.path.realpath(__file__))

    # Get the parent directory of the current script directory
    parent_directory = os.path.dirname(current_script_directory)

    # Get the grandparent directory (PrecisionRAG-AutomationSuite)
    grandparent_directory = os.path.dirname(parent_directory)
    

    file_path = os.path.join(grandparent_directory,"test-dataset/test-data.json")
    print(file_path)
    with open(file_path, 'r') as f:
        prompts = json.load(f)
    print(file_path)

    # Evaluate each prompt
    results = []
    for prompt in prompts:
        context_message = file_reader("prompts/context.txt")
        context = str(context_message)
        prompt_message = file_reader("prompts/data-generation-prompt.txt")
        prompt_text = str(prompt_message)
        # context_message=retrieve_context("5", inputText.inputText)
    
        evaluation_result = evaluate(prompt_text, prompt['prompt'], context)
        results.append({
            "prompt": prompt['prompt'],
            "classification": evaluation_result['classification'],
            "accuracy": evaluation_result['accuracy'],
            "sufficient_context": context
        })

    return results

