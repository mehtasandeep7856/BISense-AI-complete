from fastapi import APIRouter
from verification.citation.citation_checker import check_citations
router=APIRouter(prefix='/api/citations',tags=['citations'])
@router.post('/verify')
def endpoint(citations:list[dict]): return {'citations':check_citations(citations)}
