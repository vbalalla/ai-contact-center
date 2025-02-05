import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
from langchain_mistralai import MistralAIEmbeddings
from langchain_mistralai.chat_models import ChatMistralAI
from mangum import Mangum  # Add Mangum for AWS Lambda support

app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
MISTRAL_API_KEY = os.environ['MISTRAL_API_KEY']

def process_message(message):
    llm = ChatMistralAI(
        model="mistral-large-latest",
        temperature=0,
        max_retries=2,
        api_key=MISTRAL_API_KEY
        # other params...
    )

    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=MISTRAL_API_KEY
    )

    messages = [
        (
            "system",
            "You are a helpful assistant for a consultant company. give short answers.",
        ),
        ("human", message),
    ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content

@app.post('/process')
async def process(request: Request):
    data = await request.json()
    message = data.get('message', '')
    processed_message = process_message(message)
    return JSONResponse(content={'processed_message': processed_message})

# Create a handler for AWS Lambda
handler = Mangum(app)


