from django.test import TestCase
from elk.service import ElasticSearchService
 
class SearchServiceTest(TestCase):
  def setUp(self):
    self.elk_service = ElasticSearchService()
    self.elk_service.connect()
  
  def test_search(self):
    search_obj = {'query': {
        'match': {'movie_name': 'Black Adam'}}}

    resp = self.elk_service.search('movies_1',search_obj)
    self.elk_service.parse_response(resp)
