from pydantic import BaseModel,Field
class SearchRequest(BaseModel): query:str=Field(min_length=1); top_k:int=6; doc_type:str|None=None
class SearchResponse(BaseModel): query:str; results:list[dict]
