from pathlib import Path
def validate_audio(path):
 p=Path(path)
 if not p.exists() or p.stat().st_size==0: raise ValueError('Audio file is empty')
 return True
