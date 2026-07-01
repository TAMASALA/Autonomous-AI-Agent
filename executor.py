from llm import llm

def execute_plan(request,plan):

    prompt=f"""
User Request

{request}

Execution Plan

{plan}

Execute all tasks.

Generate a polished professional document.

Return markdown headings.
"""

    response=llm.invoke(prompt)

    return response.content