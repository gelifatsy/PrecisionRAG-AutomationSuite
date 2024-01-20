from fastapi import FastAPI, Form, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Chat Interface</title>
        </head>
        <body>
            <h1>Welcome to FastAPI Chat Interface</h1>
        </body>
    </html>
    """

@app.post("/process_input")
async def process_input(
    input_text: str = Form(...),
    output_type: str = Query(...),
):
    # Process the input_text and output_type
    # Perform your logic here (e.g., generate a response)
    # For now, just return the received data
    print("Received Data:")
    print("Input Text:", input_text)
    print("Output Type:", output_type)
   
    return {"input_text": input_text, "output_type": output_type}


