from elk.service import ElasticSearchService

class SearchService:
  def __init__(self):
    self.elk_service = ElasticSearchService()
    self.elk_service.connect()
  
  def search_text_field_bm25(self,search_query):
    search_obj = {
        "query": {
            "multi_match": {
                "query": search_query,
                "fields": ["movie_name",
                           "abstract", "plot", "rating",
                           "genre"]
            }
        }
    }
    resp = self.elk_service.search('movies', search_obj)
    return self.elk_service.parse_response(resp)



