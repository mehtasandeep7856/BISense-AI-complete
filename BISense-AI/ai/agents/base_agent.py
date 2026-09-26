from ai.llm.response_generator import generate_response
from rag.pipeline.retrieval_pipeline import retrieve
class BaseAgent:
 name='general'
 def run(self,query,history=None):
  e=retrieve(query); return {'answer':generate_response(query,e,history or [],self.name),'evidence':e}
