from fastapi import APIRouter,UploadFile,File
from backend.app.config import get_settings
from backend.app.services.document_service import save_upload
from backend.app.services.compliance_service import analyze_image
router=APIRouter(prefix='/api/compliance',tags=['compliance'])
@router.post('/analyze')
def endpoint(file:UploadFile=File(...)):
 p=save_upload(get_settings().uploads_dir+'/images',file.filename,file.file); return analyze_image(str(p))
