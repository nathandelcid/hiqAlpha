import asyncio
from fastapi import FastAPI
from mcp_agent.core.fastagent import FastAgent
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

class ToolInfo(BaseModel):
    name: str
    description: str

class ServerInfo(BaseModel):
    name: str
    version: str
    status: str
    endpoints: Dict[str, str]
    tools: List[ToolInfo]


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
        host="0.0.0.0",
        server_name="API-Agent-Server",
        server_description="Provides API access to my agent"
    )

if __name__ == "__main__":
    asyncio.run(start_application())