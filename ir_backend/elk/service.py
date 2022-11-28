from elasticsearch import Elasticsearch

class ElasticSearchService:
  def __init__(self) -> None:
    # Create the client instance
    self.es = Elasticsearch("http://localhost:9200")
  
  def connect(self):
    if self.es.ping():
        return True
    else:
        raise OSError(f'Failed to start elastic search')
  
  def create_index(self,idx_name,settings):
    self.delete_idx(idx_name)
    self.es.indices.create(index=idx_name, ignore=400, body=settings)

  def bulk_insert(self,action_list,idx_name):
    self.es.bulk(operations=action_list, index=idx_name)
  
  def check_idx_exist(self,idx_name):
    return self.es.indices.exists(idx_name)

  def insert_document(self, idx_name, json_data):
    self.es.index(index=idx_name,
                  document=json_data)

  def delete_idx(self,idx_name):
    self.es.options(ignore_status=[400, 404]).indices.delete(index=idx_name)

  def search(self,idx_name,q):
    resp = self.es.search(index=idx_name,body=q)
    return resp
  
  def parse_response(self,response):
    total_no_of_doc = response['hits']['total']['value']
    doc_max_score = response['hits']['max_score']
    result=[]
    for hit in response['hits']['hits']:
      hit["_source"]["score"] = hit["_score"]
      result.append(hit["_source"])
    return {
        "retrieved_doc_no": total_no_of_doc,
        "search_result":result
      }