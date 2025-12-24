from config import config
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

def load_llm(temp=0, max_tokens=800):
    if config.LLM_PROVIDER == "openai":
        return ChatOpenAI(model=config.OPENAI_MODEL, temperature=temp, api_key=config.OPENAI_API_KEY)
    return ChatGoogleGenerativeAI(model=config.GOOGLE_MODEL, temperature=temp, api_key=config.GOOGLE_API_KEY, max_output_tokens=max_tokens)