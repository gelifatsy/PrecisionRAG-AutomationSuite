import os
import sys
import json
sys.path.insert(0, '/home/elias/Documents/10 Academy/WEEK 6/PrecisionRAG-AutomationSuite')
from data_generation import _data_generation, _evaluation, retrive_context,evaluate

query="tasks in this week challenge"
context=retrive_context.retrieve_context(query)
prompts = _data_generation.main("5")
evaluation= evaluate.evaluate()
print(evaluation)

print(prompts)  # This now prints the list of JSON objects without the "prompts" key

    # Evaluate each prompt

   


# evaluation=_evaluation.main()

# from fastapi import FastAPI, Body

# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Update with your frontend URL
#     allow_credentials=True,
#     allow_methods=["GET", "POST"],
#     allow_headers=["*"],
# )

# class Query(BaseModel):
#     query: str



# @app.post("/answer")
# async def answer(query: Query):
#     """Receives a query from the frontend and returns the answer."""
#     prompt = generate_test_data(query.query)
#     test=eva
#     return {"answer": response}

