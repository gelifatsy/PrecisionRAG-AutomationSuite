


        

from fastapi import FastAPI, Body

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str



@app.post("/answer")
async def answer(query: Query):
    """Receives a query from the frontend and returns the answer."""
    prompt = generate_test_data(query.query)
    test=eva
    return {"answer": response}

