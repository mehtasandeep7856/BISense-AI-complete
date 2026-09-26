from fastapi import APIRouter
from ai.conversation.history import get_history
router=APIRouter(prefix='/api/history',tags=['history'])
@router.get('/{session_id}')
def endpoint(session_id): return {'session_id':session_id,'messages':get_history(session_id)}
