from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from backend.app.config import get_settings
from backend.app.utils.auth import create_access_token
router=APIRouter(prefix='/api/auth',tags=['auth'])
class LoginRequest(BaseModel): username:str; password:str
@router.post('/login')
def endpoint(r:LoginRequest):
 s=get_settings()
 if r.username!=s.demo_username or r.password!=s.demo_password: raise HTTPException(401,'Invalid credentials')
 return {'access_token':create_access_token(r.username),'token_type':'bearer'}
