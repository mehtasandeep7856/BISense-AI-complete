from ai.conversation.history import get_history,append_message
from ai.graph.workflow import run_workflow
def chat(message,session_id='default',language=None):
 h=get_history(session_id); append_message(session_id,'user',message); s=run_workflow(message,session_id,h,language); append_message(session_id,'assistant',s['answer']); return s
