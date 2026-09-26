from fastapi import APIRouter,UploadFile,File
from backend.app.config import get_settings
from backend.app.services.document_service import save_upload
from vision.product.label_scanner import scan_label
router=APIRouter(prefix='/api/labels',tags=['labels'])
@router.post('/scan')
def endpoint(file:UploadFile=File(...)):
 p=save_upload(get_settings().uploads_dir+'/images',file.filename,file.file); return scan_label(str(p))
