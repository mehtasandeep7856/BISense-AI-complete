from pathlib import Path
def validate_source(source): return bool(source) and (Path(source).suffix.lower() in {'.pdf','.csv','.txt'} or source.startswith('http'))
