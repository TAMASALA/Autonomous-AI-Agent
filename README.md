# Autonomous AI Agent

An end-to-end autonomous AI agent built using **FastAPI**, **LangChain**, **Groq Llama 3.3**, and **python-docx**.

The agent accepts natural language requests, creates its own execution plan, executes each task autonomously, reviews its output, and generates a polished Microsoft Word document.

---

## Features

- FastAPI REST API
- Autonomous Task Planning
- LLM-based Execution
- Self Reflection / Quality Check
- Professional DOCX Generation
- Modular Architecture
- Free LLM (Groq)

---

## Tech Stack

- Python
- FastAPI
- LangChain
- Groq Llama 3.3
- python-docx
- Pydantic
- Uvicorn

---

## Project Structure

```
autonomous-agent/
│
├── app.py
├── agent.py
├── planner.py
├── executor.py
├── reflector.py
├── document_generator.py
├── llm.py
├── models.py
├── generated_docs/
├── requirements.txt
└── README.md
```

---

## API

### POST /agent

Request

```json
{
    "request":"Create a project proposal for an AI chatbot."
}
```

Response

```json
{
  "plan":[
      "...tasks..."
  ],
  "content":"Generated document",
  "document":"generated_docs/xxxxx.docx"
}
```

---

## Engineering Improvement

This project implements **Reflection / Self-Check**.

Before generating the final Word document, the AI reviews its own output for:

- Grammar
- Missing Sections
- Professional Writing
- Formatting
- Completeness

The reviewed version is used for the final document.

---

## Example Requests

### Business Request

```
Create a project proposal for an AI Customer Support Chatbot.
```

### Complex Request

```
We need an AI solution for a retail company.

Budget is small.

Timeline is short.

We don't know whether to build a chatbot, recommendation engine, or forecasting solution.

Create the best proposal with assumptions.
```

---

## Run

Install dependencies

```
pip install -r requirements.txt
```

Start server

```
uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Architecture

```
User Request
      │
      ▼
 FastAPI Endpoint
      │
      ▼
 Autonomous Planner
      │
      ▼
 Task Execution
      │
      ▼
 Reflection
      │
      ▼
 DOCX Generator
      │
      ▼
 Final Response
```

---

## Assignment Requirements Covered

- FastAPI API
- Autonomous Planning
- Natural Language Understanding
- Multi-step Task Execution
- Word Document Generation
- Free LLM Integration
- Engineering Improvement
- Modular Codebase
