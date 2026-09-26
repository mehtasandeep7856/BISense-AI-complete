from pydantic import BaseModel
class Document(BaseModel): id:str; source:str; doc_type:str='unknown'; title:str=''; text:str
