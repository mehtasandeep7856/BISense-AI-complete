from rag.retrieval.bm25_search import tok
def test_tok(): assert tok('BIS IS 1234')==['bis','is','1234']
