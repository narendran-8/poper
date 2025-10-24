from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os, asyncio

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file!")
else:
    print("Key imported successfully!")



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)


async def main():
    client = MultiServerMCPClient(
        {
            "OWN_TOOL": {
                "command":"python3",
                "args":["own_tools.py"],
                "transport":"stdio"
            }
        }
    )


    tools = await client.get_tools()

    agent = create_react_agent(llm, tools)

    mcp_res = await agent.ainvoke(
        {"messages":[{"role":"user", "content":"increase this number 999"}]}
    )

    print(mcp_res)

    print(mcp_res["messages"][-1].content)

asyncio.run(main())