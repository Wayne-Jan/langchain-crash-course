import os
from langchain_openai import AzureChatOpenAI, AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    api_version=os.getenv('OPENAI_API_VERSION'),
    azure_endpoint=os.getenv('OPENAI_DEPLOYMENT_ENDPOINT'),    
)

def get_chat_model(temperature=0.8):

    return AzureChatOpenAI(
        openai_api_key=os.getenv('OPENAI_API_KEY'),
        openai_api_type=os.getenv('OPENAI_API_TYPE'),
        azure_endpoint=os.getenv('OPENAI_DEPLOYMENT_ENDPOINT'),
        openai_api_version=os.getenv('OPENAI_API_VERSION'),
        deployment_name=os.getenv('OPENAI_DEPLOYMENT_NAME'),
        model_name=os.getenv('OPENAI_MODEL_NAME'),
        temperature=temperature
    )

def generate_embeddings(text, model=os.getenv('OPENAI_WORD_NAME')):

    return client.embeddings.create(input = [text], model=model).data[0].embedding

