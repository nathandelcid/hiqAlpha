import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from mcp_agent.core.fastagent import FastAgent

class PromptRequest(BaseModel):
    prompt: str

app = FastAPI()

fast = FastAgent("hIqAgent")

@fast.agent(
    "hiq-mcp",
    instruction = "You are Maestro, a helpful music producing assistant developed by Harmoniq",
    servers = ["HarmoniqMCP"]
)
   
@app.post("/chat")
async def chat(request: PromptRequest):
    async with fast.run() as agent:
        user_message = request.prompt
        response_text = await agent.send(user_message)
        return {"response": response_text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)