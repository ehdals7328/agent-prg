import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#OpenAi Embedding model AIP KEY
EMBEDDING_MODEL = "text-embedding-3-small"
#EMBEDDING_MODEL = "text-embedding-ada-002"

if not OPENAI_API_KEY:
    raise ValueError("API KEY를 찾을 수 없습니다.")