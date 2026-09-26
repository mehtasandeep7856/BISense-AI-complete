from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import get_settings
from backend.app.api import chat,search,standards,certification,qco,laboratories,hallmarking,consumer,documents,compliance,labels,citations,auth,history,voice

s=get_settings(); app=FastAPI(title=s.app_name,version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=s.cors_list,allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
for r in [chat.router,search.router,standards.router,certification.router,qco.router,laboratories.router,hallmarking.router,consumer.router,documents.router,compliance.router,labels.router,citations.router,auth.router,history.router,voice.router]: app.include_router(r)
@app.get('/')
def root(): return {'name':s.app_name,'status':'running'}
@app.get('/health')
def health(): return {'status':'ok'}
