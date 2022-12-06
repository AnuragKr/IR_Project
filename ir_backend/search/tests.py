from django.test import TestCase
from elk.service import ElasticSearchService
from search.service import SearchService
 
class SearchServiceTest(TestCase):
  def setUp(self):
    self.searchService = SearchService()
    self.elk_service = ElasticSearchService()
    self.elk_service.connect()
  
  def test_search(self):
    # search_obj = {
    #     "query": {
    #         "bool": {
    #             "must": [{
    #                 "term": {
    #                      "movie_name": "star"
    #                      }
    #             }
    #             ]
    #         }
    #     }
    # }

    # print(search_obj)
    search_obj = {
        "query": {
          "bool": 
          {
            "must": [
            {"term": 
              {"movie_name": "black adam"}
            }]
          }
        }
      }
    # search_obj = {
    #     "size": 5,
    #     "query": {
    #         "multi_match": {
    #             "query": "bl",
    #             "type": "bool_prefix",
    #             "fields": [
    #                 "movie_name",
    #                 "movie_name._2gram",
    #                 "movie_name._3gram",
    #             ]
    #         }
    #     }
    # }

    search_obj = {
        'query': {'bool': 
        {'must': [{'term': {'movie_name': 'black'}}]}}}
    query_obj = {'movie_name': 'black'}

    resp = self.searchService.search_phrase_text_field_bm25(query_obj)
    print(resp)
    # resp = self.searchService.search_text_tf_idf('black')
    # resp = self.elk_service.search('movies_tf_idf', search_obj)
    # print(self.elk_service.parse_response(resp))
