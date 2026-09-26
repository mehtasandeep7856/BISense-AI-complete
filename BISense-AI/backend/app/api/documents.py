from fastapi import APIRouter,UploadFile,File
from backend.app.config import get_settings
from backend.app.services.document_service import save_upload
router=APIRouter(prefix='/api/documents',tags=['documents'])
@router.post('/upload')
def endpoint(file:UploadFile=File(...)):
 p=save_upload(get_settings().uploads_dir+'/pdf',file.filename,file.file); return {'filename':file.filename,'saved_path':str(p),'size':p.stat().st_size,'content_type':file.content_type}
