from elasticsearch import Elasticsearch

class ElasticSearchService:
  def __init__(self) -> None:
    # Create the client instance
    self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
  
  def connect(self):
    if self.es.ping():
        return True
    else:
        return False
