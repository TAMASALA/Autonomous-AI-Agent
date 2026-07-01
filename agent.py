from planner import create_plan
from executor import execute_plan
from reflector import review
from document_generator import create_doc

def run_agent(request):

    plan=create_plan(request)

    draft=execute_plan(request,plan)

    final=review(draft)

    doc=create_doc(final)

    return {
        "plan":plan,
        "content":final,
        "document":doc
    }