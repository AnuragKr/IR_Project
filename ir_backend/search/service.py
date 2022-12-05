from elk.service import ElasticSearchService

class SearchService:
  def __init__(self):
    self.elk_service = ElasticSearchService()
    self.elk_service.connect()
  
  def search_text_bm25(self,search_query):
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

  def search_text_tf_idf(self, search_query):
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
    resp = self.elk_service.search('movies_tf_idf', search_obj)
    return self.elk_service.parse_response(resp)

  def search_fuzzy_text_bm25(self, search_query):
    #Link -> https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness
    search_obj = {
        "query": {
            "multi_match": {
                "query": search_query,
                "fields": ["movie_name","abstract"],
                "fuzziness": "AUTO"
            }
        }
    }
    resp = self.elk_service.search('movies', search_obj)
    return self.elk_service.parse_response(resp)

  def search_auto_text_bm25(self, search_query):
    #Link -> https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness
    search_obj = {
        "size":5,
        "query": {
            "multi_match": {
                "query": search_query,
                "type": "bool_prefix",
                "fields": [
                    "movie_name",
                    "movie_name._2gram",
                    "movie_name._3gram",
                ]
            }
        }
    }
    resp = self.elk_service.search('autocomplete', search_obj)
    return self.elk_service.parse_response(resp)

  def search_text_field_bm25(self, search_query):
    query_obj = []
    for key,value in search_query.items():
        query_obj.append({'term':
                          {key: value}})

    search_obj = {'query':
     {'bool':
        {'must':query_obj}
     }
    }
    print(search_obj)
    resp = self.elk_service.search('movies', search_obj)
    return self.elk_service.parse_response(resp)

  def search_text_field_tf_idf(self, search_query):
    query_obj = []
    for key, value in search_query.items():
        query_obj.append({'term':
                          {key: value}})

    search_obj = {'query':
                  {'bool':
                   {'must': query_obj}
                   }
                  }
    print(search_obj)
    resp = self.elk_service.search('movies', search_obj)
    return self.elk_service.parse_response(resp)



