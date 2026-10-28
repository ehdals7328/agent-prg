from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

# MCP 서버 생성
mcp = FastMCP("SearchServer")

# 1. LlamaIndex 문서 로드 및 인덱싱
llama_docs = SimpleDirectoryReader("./llamaindex_docs").load_data()
llama_index = VectorStoreIndex.from_documents(llama_docs)
llama_query_engine = llama_index.as_query_engine()

# 2. GitHub 문서 로드 및 인덱싱
github_docs = SimpleDirectoryReader("./github_docs").load_data()
github_index = VectorStoreIndex.from_documents(github_docs)
github_query_engine = github_index.as_query_engine()


# 3. MCP Tool 등록
@mcp.tool()
def search_llama_docs(query: str) -> str:
    """llamaindex 문서에서 질의에 맞는 내용을 검색합니다."""
    response = llama_query_engine.query(query)
    return str(response)


@mcp.tool()
def search_github_docs(query: str) -> str:
    """깃허브 문서에서 질의에 맞는 내용을 검색합니다."""
    response = github_query_engine.query(query)
    return str(response)


if __name__ == "__main__":
    # SSE 트랜스포트로 실행 (기본 포트 8000)
    mcp.run(transport="sse")