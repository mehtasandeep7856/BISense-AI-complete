from datetime import datetime,timezone
def freshness_status(modified_iso,max_age_days=365):
 d=datetime.fromisoformat(modified_iso); d=d.replace(tzinfo=timezone.utc) if d.tzinfo is None else d; age=(datetime.now(timezone.utc)-d).days; return {'age_days':age,'fresh':age<=max_age_days}
