from functools import lru_cache
from backend.app.config import get_settings
@lru_cache
def get_embedding_model():
 from sentence_transformers import SentenceTransformer
 return SentenceTransformer(get_settings().embedding_model)
