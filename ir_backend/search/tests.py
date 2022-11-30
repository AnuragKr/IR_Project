from django.test import TestCase
from elk.service import ElasticSearchService
 
class SearchServiceTest(TestCase):
  def setUp(self):
    self.elk_service = ElasticSearchService()
    self.elk_service.connect()
  
  def test_search(self):
    # search_obj = {
    #     "query": {
    #         "multi_match": {
    #             "query": "black adam",
    #             "fields": ["movie_name",
    #                        "abstract", "plot", "rating", 
    #                        "genre"]
    #         }
    #     }
    # }

    search_obj = {
        "size": 5,
        "query": {
            "multi_match": {
                "query": "bl",
                "type": "bool_prefix",
                "fields": [
                    "movie_name",
                    "movie_name._2gram",
                    "movie_name._3gram",
                ]
            }
        }
    }
    resp = self.elk_service.search('autocomplete',search_obj)
    result = self.elk_service.parse_response(resp)
    print(result)
