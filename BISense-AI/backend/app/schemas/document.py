from pydantic import BaseModel
class DocumentResponse(BaseModel): filename:str; saved_path:str; size:int; content_type:str
