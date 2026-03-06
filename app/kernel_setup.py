import os
from dotenv import load_dotenv
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from openai import AsyncOpenAI

load_dotenv()

def create_kernel():

    kernel = sk.Kernel()

    # Create async client for NVIDIA endpoint
    client = AsyncOpenAI(
        api_key=os.getenv("NVIDIA_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    service = OpenAIChatCompletion(
        service_id="chat",
        ai_model_id=os.getenv("MODEL_NAME"),
        async_client=client
    )

    kernel.add_service(service)

    return kernel