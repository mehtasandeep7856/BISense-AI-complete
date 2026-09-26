from pathlib import Path
import shutil,uuid
def save_upload(directory,filename,file_obj):
 p=Path(directory); p.mkdir(parents=True,exist_ok=True); out=p/(uuid.uuid4().hex+Path(filename).suffix.lower());
 with out.open('wb') as f: shutil.copyfileobj(file_obj,f)
 return out
