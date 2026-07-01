from llm import llm

def create_plan(user_request):

    prompt=f"""
You are an autonomous AI agent.

User Request:
{user_request}

Create a numbered TODO list.

Example

1. Understand request
2. Identify document type
3. Create outline
4. Generate content
5. Review quality
6. Produce final document

Only return numbered tasks.
"""

    response=llm.invoke(prompt)

    tasks=response.content.split("\n")

    return [t for t in tasks if t.strip()]