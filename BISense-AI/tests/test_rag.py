from rag.processing.chunker import chunk_text
def test_chunk(): assert chunk_text('x'*1000,200,20)
