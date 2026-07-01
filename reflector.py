from llm import llm

def review(content):

    prompt=f"""
Review the following business document.

Check

- grammar
- missing sections
- formatting
- professionalism

If improvements needed rewrite.

Document

{content}
"""

    response=llm.invoke(prompt)

    return response.content