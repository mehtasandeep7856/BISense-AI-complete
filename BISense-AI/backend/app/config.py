from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name:str='BISense AI'; environment:str='development'; api_host:str='0.0.0.0'; api_port:int=8000
    cors_origins:str='http://localhost:5173'; groq_api_key:str=''; groq_model:str='llama-3.3-70b-versatile'
    embedding_model:str='sentence-transformers/all-MiniLM-L6-v2'; reranker_model:str='cross-encoder/ms-marco-MiniLM-L-6-v2'
    enable_reranker:bool=True; top_k:int=6; chunk_size:int=800; chunk_overlap:int=120
    tesseract_cmd:str=''; ocr_engine:str='auto'; whisper_model:str='base'; default_tts_language:str='en'
    jwt_secret:str='change-me'; jwt_algorithm:str='HS256'; access_token_minutes:int=60; demo_username:str='admin'; demo_password:str='change-me'
    data_dir:str='data'; raw_data_dir:str='data/raw'; processed_data_dir:str='data/processed'; documents_dir:str='data/documents'; uploads_dir:str='data/uploads'; vector_db_dir:str='vector_db'
    model_config=SettingsConfigDict(env_file='.env',extra='ignore',case_sensitive=False)
    @property
    def cors_list(self): return [x.strip() for x in self.cors_origins.split(',') if x.strip()]
    def ensure_dirs(self):
        for p in [self.raw_data_dir,self.processed_data_dir,self.documents_dir,self.uploads_dir,self.vector_db_dir,f'{self.uploads_dir}/images',f'{self.uploads_dir}/audio',f'{self.uploads_dir}/pdf',f'{self.vector_db_dir}/faiss',f'{self.vector_db_dir}/bm25']:
            Path(p).mkdir(parents=True,exist_ok=True)

@lru_cache
def get_settings():
    s=Settings(); s.ensure_dirs(); return s
