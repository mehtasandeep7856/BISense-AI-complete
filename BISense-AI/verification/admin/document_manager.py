from pathlib import Path
def list_documents(directory): return [str(p) for p in Path(directory).rglob('*') if p.is_file()]
