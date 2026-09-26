from fastapi import Header, HTTPException

def optional_token(authorization: str | None = Header(default=None)):
    if not authorization:
        return None
    if not authorization.startswith('Bearer '):
        raise HTTPException(status_code=401, detail='Invalid authorization header')
    return authorization[7:]
