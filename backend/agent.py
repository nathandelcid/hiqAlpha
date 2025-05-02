import asyncio
from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("fast-agent")

@fast.agent(
    "ableton_mcp",
    instruction = "You are Maestro, a helpful music producing assistant developed by Harmoniq",
    servers = ["HarmoniqMCP"]
)

async def mcp_agent():
    async with fast.run() as agent:
        await agent()

async def start_application():
    await fast.start_server(
        transport="sse",
        # port=8080
    )

if __name__ == "__main__":
    asyncio.run(start_application())