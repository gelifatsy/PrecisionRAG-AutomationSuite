from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import json
sys.path.insert(0, '/home/elias/Documents/10 Academy/WEEK 6/PrecisionRAG-AutomationSuite')

from data_generation_evaluation import prompt_generation, retrieval, evaluation


app = FastAPI()

app.add_middleware(
    
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["GET", "POST","OPTION"],
    allow_headers=["*"],
)

class Input(BaseModel):
    query: str

@app.post("/gep")
async def generate_and_evaluate_prompts(query: Input):
    # Generate prompt data
    
    context= retrieval.retrieve_context(query.query)
    prompts= prompt_generation.main("5")
    print(prompts)
    
  # Read the generated prompts
    script_dir = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.dirname(script_dir)
    file_path = os.path.join(base_dir, "test-dataset/test-data4.json")
    with open(file_path, 'r') as f:
        prompts = json.load(f)
    
    
    # questions = [item["prompt"] for item in prompts["prompts"]]
    # print(questions)

    # Evaluate each prompt
    results = []
    for prompt  in prompts:
            context_message = context
            context = str(context_message)
            prompt_path = "/home/elias/Documents/10 Academy/WEEK 6/PrecisionRAG-AutomationSuite/prompts/generic-evaluation-prompt.txt"
            prompt_message = prompt_generation.file_reader(prompt_path)
            prompt_text = str(prompt_message)
            # question_str = str(questions)
            evaluation_result = evaluation.evaluate(prompt_text, prompt['prompt'], context)
            results.append({
                "prompt": prompt['prompt'],
                "classification": evaluation_result['classification'],
                "accuracy": evaluation_result['accuracy'],
                "sufficient_context": context
            })
        

    return results


# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     file_location = f"/home/mubarek/all_about_programing/10x_projects/Enterprise-Level-Automated-Prompt-Engineering/backend/pdfs/{file.filename}"
#     with open(file_location, "wb+") as file_object:
#         file_object.write(await file.read())
#     return {"info": f"file '{file.filename}' stored at location: '{file_location}'"}