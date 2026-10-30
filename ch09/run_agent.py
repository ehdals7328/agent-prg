import asyncio
from dotenv import load_dotenv
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

load_dotenv()


async def main():
    # 노트북의 IPv4 주소와 8000 포트로 지정합니다.
    notebook_ip = "192.168.0.25"  # <-- 여기에 확인한 노트북 IP 입력
    mcp_client = BasicMCPClient(f"http://{notebook_ip}:8000/sse")

    try:
        # 노트북의 MCP 서버에 연결하여 도구 목록 원격 로드
        await mcp_client.connect()
        mcp_tool_spec = McpToolSpec(client=mcp_client)
        tools = mcp_tool_spec.to_tool_list()

        # LLM 및 Agent 설정
        llm = OpenAI(model="gpt-4o-mini")
        agent = FunctionAgent(
            tools=tools,
            llm=llm,
            system_prompt="노트북 MCP 서버의 문서 검색 도구를 활용하여 답변하는 에이전트입니다.",
        )

        # 테스트 질문 실행
        question = "Llama-Index를 활용하여 문서 검색하는 방법"
        print(f"질문: {question}\n")

        response = await agent.run(question)
        print("== 에이전트 응답 ==")
        print(response)

    finally:
        if hasattr(mcp_client, "close"):
            await mcp_client.close()


if __name__ == "__main__":
    asyncio.run(main())