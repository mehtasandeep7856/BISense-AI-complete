from functools import lru_cache
from backend.app.config import get_settings
from voice.stt.audio_processor import validate_audio
@lru_cache
def get_whisper_model():
 import whisper; return whisper.load_model(get_settings().whisper_model)
def transcribe(path):
 validate_audio(path); r=get_whisper_model().transcribe(path,fp16=False); return {'text':r.get('text','').strip(),'language':r.get('language','en'),'segments':r.get('segments',[])}
