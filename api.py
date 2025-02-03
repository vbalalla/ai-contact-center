import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_mistralai import MistralAIEmbeddings
from langchain_mistralai.chat_models import ChatMistralAI


app = Flask(__name__)
CORS(app)
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

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    message = data.get('message', '')
    processed_message = process_message(message)
    return jsonify({'processed_message': processed_message})

if __name__ == '__main__':
    app.run(debug=True, port=5002)


