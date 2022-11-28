from django.test import TestCase
from elk.service import ElasticSearchService
 
class SearchServiceTest(TestCase):
  def setUp(self):
    self.elk_service = ElasticSearchService()
    self.elk_service.connect()
  
  def test_search(self):
    search_obj = {
        "query": {
            "multi_match": {
                "query": "black adam",
                "fields": ["movie_name",
                           "abstract", "plot", "rating", 
                           "genre"]
            }
        }
    }
    resp = self.elk_service.search('movies',search_obj)
    result = self.elk_service.parse_response(resp)
    print(result)
