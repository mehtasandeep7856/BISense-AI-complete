from pathlib import Path
import uuid
def new_audio_path(directory,suffix='.mp3'):
 Path(directory).mkdir(parents=True,exist_ok=True); return str(Path(directory)/(uuid.uuid4().hex+suffix))
