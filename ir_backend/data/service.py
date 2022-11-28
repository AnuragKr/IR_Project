from elk.service import ElasticSearchService
from pathlib import Path
import json,glob

class DataService:
  def __init__(self):
    self.elk_service = ElasticSearchService()
    self.elk_service.connect()

  def create_index(self,idx_name):
    idx_name = idx_name
    idx_setting = {
         "settings": {
             "number_of_shards": 1,
             "number_of_replicas": 0
         },
         "mappings": {
                "dynamic": "strict",
                 "properties": {
                     "movie_name": {
                         "type": "string"
                     },
                     "year": {
                         "type": "date"
                     },
                     "rating": {
                         "type": "string"
                     },
                     "genre": {
                         "type": "text"
                     },
                     "imdb": {
                         "type": "double"
                     },
                     "plot":{
                      "type": "text"
                     }
                 }
         }
     }
    self.elk_service.create_index(idx_name,idx_setting)

  def insert_data(self):
    idx_name = 'movies_1'
    self.create_index(idx_name)
    with open('data/static/movies.json', 'r') as j:
     contents = json.loads(j.read())
     for movie in contents:
      try:
        self.elk_service.insert_document(idx_name,movie)
      except Exception as err:
        print(movie)
        print('-----------')

    return len(contents)
