from fastapi import APIRouter,UploadFile,File
from fastapi.responses import FileResponse
from backend.app.config import get_settings
from backend.app.services.document_service import save_upload
from voice.stt.whisper_service import transcribe
from voice.tts.tts_service import synthesize
from voice.utils.audio_utils import new_audio_path
router=APIRouter(prefix='/api/voice',tags=['voice'])
@router.post('/transcribe')
def transcribe_endpoint(file:UploadFile=File(...)):
 p=save_upload(get_settings().uploads_dir+'/audio',file.filename,file.file); return transcribe(str(p))
@router.post('/speak')
def speak(text:str,language='en'):
 p=new_audio_path(get_settings().uploads_dir+'/audio'); synthesize(text,p,language); return FileResponse(p,media_type='audio/mpeg',filename=p.split('/')[-1])
