from rag.pipeline.retrieval_pipeline import retrieve
def search(query,top_k=6,doc_type=None): return retrieve(query,top_k,doc_type)
