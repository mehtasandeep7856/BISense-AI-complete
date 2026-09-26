from fastapi import APIRouter
from rag.pipeline.retrieval_pipeline import retrieve
router=APIRouter(prefix='/api/consumer',tags=['consumer'])
@router.get('')
def endpoint(q:str,top_k:int=6): return {'query':q,'results':retrieve(q,top_k)}
