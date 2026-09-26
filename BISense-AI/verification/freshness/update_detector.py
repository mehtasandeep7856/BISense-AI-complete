from pathlib import Path
from datetime import datetime
def scan_for_updates(directory): return sorted([{'path':str(p),'modified':datetime.fromtimestamp(p.stat().st_mtime).isoformat(),'size':p.stat().st_size} for p in Path(directory).rglob('*') if p.is_file()],key=lambda x:x['modified'],reverse=True)
