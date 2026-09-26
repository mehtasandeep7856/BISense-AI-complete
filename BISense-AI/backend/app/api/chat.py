from fastapi import APIRouter
from backend.app.schemas.chat import ChatRequest,ChatResponse
from backend.app.services.chat_service import chat
router=APIRouter(prefix='/api/chat',tags=['chat'])
@router.post('',response_model=ChatResponse)
def endpoint(r:ChatRequest):
 s=chat(r.message,r.session_id,r.language); return ChatResponse(answer=s['answer'],intent=s.get('intent','general'),session_id=r.session_id,citations=s.get('citations',[]),evidence=s.get('evidence',[]))
