from fastapi import FastAPI
from models import AgentRequest
from agent import run_agent

app = FastAPI(title="Autonomous AI Agent")


@app.get("/")
def home():
    return {
        "message": "Vinay is Aiming for AI Roles in entry level positions. This is an Autonomous AI Agent that can perform tasks based on user input.",
        "docs": "/docs"
    }


@app.post("/agent")
def agent(req: AgentRequest):
    return run_agent(req.request)