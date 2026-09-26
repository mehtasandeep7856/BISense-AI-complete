from datetime import datetime,timedelta,timezone
import jwt
from backend.app.config import get_settings
def create_access_token(sub):
 s=get_settings(); return jwt.encode({'sub':sub,'exp':datetime.now(timezone.utc)+timedelta(minutes=s.access_token_minutes)},s.jwt_secret,algorithm=s.jwt_algorithm)
def decode_access_token(token):
 s=get_settings(); return jwt.decode(token,s.jwt_secret,algorithms=[s.jwt_algorithm])
