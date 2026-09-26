from pydantic import BaseModel
class ComplianceFinding(BaseModel): field:str; value:str|None=None; status:str; reason:str; evidence:list[dict]=[]
