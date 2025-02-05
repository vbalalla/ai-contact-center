# AI Contact Center

This project is an AI-powered contact center application using FastAPI, LangChain, and AWS Lambda.

## Prerequisites

- Python 3.9
- AWS SAM CLI
- Docker (for building and testing locally)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-repo/ai-contact-center.git
    cd ai-contact-center
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt --platform manylinux2014_x86_64 --target ./python --only-binary=:all:
    ```

## Building and Testing Locally with AWS SAM

1. **Build the SAM application**:
    ```sh
    sam build
    ```

2. **Start the local API**:
    ```sh
    sam local start-api
    ```

3. **Invoke the function**:
    You can use `curl` or any HTTP client to send a request to your local API Gateway.
    ```sh
    curl -X POST http://127.0.0.1:3000/process -H "Content-Type: application/json" -d '{"message": "Hello"}'
    ```

## Docker Deployment

1. **Build the Docker image**:
    ```sh
    docker build -t ai-contact-center --build-arg MISTRAL_API_KEY=your_api_key_here .
    ```

2. **Run the Docker container**:
    ```sh
    docker run -p 8000:8000 -e MISTRAL_API_KEY=your_api_key_here ai-contact-center
    ```

3. **Access the application**:
    Open your browser and go to `http://localhost:8000`.

## AWS Lambda Deployment

1. **Package the application**:
    ```sh
    sam package --output-template-file packaged.yaml --s3-bucket your-s3-bucket
    ```

2. **Deploy the application**:
    ```sh
    sam deploy --template-file packaged.yaml --stack-name ai-contact-center --capabilities CAPABILITY_IAM --parameter-overrides MistralApiKey=your_api_key_here
    ```

## Environment Variables

- `MISTRAL_API_KEY`: API key for Mistral AI.

## License

This project is licensed under the MIT License.