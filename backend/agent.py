import asyncio
from fastapi import FastAPI
from mcp_agent.core.fastagent import FastAgent
from pydantic import BaseModel
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
    )

if __name__ == "__main__":
    asyncio.run(start_application())