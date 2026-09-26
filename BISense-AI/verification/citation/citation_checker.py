from verification.citation.source_validator import validate_source
def check_citations(citations): return [{**c,'valid_source':validate_source(c.get('source',''))} for c in citations]
