from pydantic import BaseModel,Field
class ChatRequest(BaseModel): message:str=Field(min_length=1); session_id:str='default'; language:str|None=None
class Citation(BaseModel): source:str; page:int|None=None; chunk_id:str|None=None; score:float|None=None
class ChatResponse(BaseModel): answer:str; intent:str; session_id:str; citations:list[Citation]=[]; evidence:list[dict]=[]
