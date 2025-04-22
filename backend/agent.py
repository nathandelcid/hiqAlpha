import asyncio
from fastapi import FastAPI
from mcp_agent.core.fastagent import FastAgent
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
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

@app.get("/", response_model=ServerInfo)
async def health_check():
    return ServerInfo(
        name="Harmoniq MCP Server",
        version="1.0.0",
        status="running",
        endpoints={
            "/": "Server information (this response)",
            "/sse": "Server-Sent Events endpoint for MCP connection",
        },
        tools=[
            ToolInfo(
                name="ableton_mcp",
                description="Music producing assistant developed by Harmoniq"
            )
        ]
    )

@app.get("/sse")
async def sse_endpoint():
    async def event_generator():
        while True:
            yield f"data: Hello\n\n"
            await asyncio.sleep(1)
    
    response = StreamingResponse(event_generator(), media_type="text/event-stream")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

fast = FastAgent("fast-agent example")

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
        port=8080,
        server_name="API-Agent-Server",
        server_description="Provides API access to my agent"
    )

if __name__ == "__main__":
    asyncio.run(start_application())