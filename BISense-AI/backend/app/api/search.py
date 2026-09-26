from fastapi import APIRouter
from backend.app.schemas.search import SearchRequest,SearchResponse
from backend.app.services.search_service import search
router=APIRouter(prefix='/api/search',tags=['search'])
@router.post('',response_model=SearchResponse)
def endpoint(r:SearchRequest): return SearchResponse(query=r.query,results=search(r.query,r.top_k,r.doc_type))
