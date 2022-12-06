from elk.service import ElasticSearchService
import json


class DataService:
    def __init__(self):
        self.elk_service = ElasticSearchService()
        self.elk_service.connect()

    def create_index(self, idx_name):
        #Link - https://stackoverflow.com/questions/71391983/removing-special-characters-and-words-from-a-url-elasticsearch
        idx_name = idx_name
        idx_setting = {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "basic_analyzer": {
                            "tokenizer": "letter",
                            "filter": [
                                "lowercase",
                                "stop",
                                "stemmer"
                            ]
                        }
                    }
                }
            },
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "movie_name": {
                        "type": "text",
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
                    "metascore": {
                        "type": "integer",
                        "include_in_all": False,
                        "index": "no"
                    },
                    "runtime_min": {
                        "type": "integer"
                    },
                    "votes": {
                        "type": "integer",
                        "include_in_all": False,
                        "index": "no"
                    },
                    "runtime_min": {
                        "type": "integer"
                    },
                    "abstract": {
                        "type": "string",
                        "analyzer": "basic_analyzer",
                    },
                    "plot": {
                        "type": "string",
                        "analyzer": "basic_analyzer",
                    },
                    "movie_link": {
                        "type": "string",
                        "include_in_all": False,
                        "index": "no"
                    },
                    "poster_link": {
                        "type": "string",
                        "include_in_all": False,
                        "index": "no"
                    }
                }
            }
        }
        self.elk_service.create_index(idx_name, idx_setting)
    
    def create_tf_idf_index(self, idx_name):
        #Link - https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html
        idx_name = idx_name
        idx_setting = {
                "settings": {
                    "similarity": {
                        "default": {
                            "type": "scripted",
                            "script": {
                                "source": "double tf = Math.sqrt(doc.freq); double idf = Math.log((field.docCount+1.0)/(term.docFreq+1.0)) + 1.0; double norm = 1/Math.sqrt(doc.length); return query.boost * tf * idf * norm;"
                            }
                        }
                    },
                "analysis": {
                    "analyzer": {
                        "basic_analyzer": {
                            "tokenizer": "letter",
                            "filter": [
                                "lowercase",
                                "stop",
                                "stemmer"
                            ]
                        }
                    }
                }
            },
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "movie_name": {
                        "type": "text",
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
                    "metascore": {
                        "type": "integer",
                        "include_in_all": False,
                        "index": "no"
                    },
                    "runtime_min": {
                        "type": "integer"
                    },
                    "votes": {
                        "type": "integer",
                        "include_in_all": False,
                        "index": "no"
                    },
                    "runtime_min": {
                        "type": "integer"
                    },
                    "abstract": {
                        "type": "string",
                        "analyzer": "basic_analyzer",
                    },
                    "plot": {
                        "type": "string",
                        "analyzer": "basic_analyzer",
                    },
                    "movie_link": {
                        "type": "string",
                        "include_in_all": False,
                        "index": "no"
                    },
                    "poster_link": {
                        "type": "string",
                        "include_in_all": False,
                        "index": "no"
                    }
                }
            }
        }
        self.elk_service.create_index(idx_name, idx_setting)

    def create_auto_index(self, idx_name):
        idx_name = idx_name
        idx_setting = {
                "mappings": {
                    "properties": {
                        "movie_name": {
                            "type": "search_as_you_type",
                        },
                        "genre": {
                            "type": "search_as_you_type"
                        }
                    }
                }
            }
        self.elk_service.create_index(idx_name, idx_setting)

    
    def insert_data(self):
        idx_name = 'movies'
        self.create_index(idx_name)
        with open('data/static/movies_cleaned.json', 'r') as j:
            contents = json.loads(j.read())
            for movie in contents:
                try:
                    self.elk_service.insert_document(idx_name, movie)
                except Exception as err:
                    continue

        print("Data inserted for model BM25 successfully.")
        return len(contents)

    def insert_auto_data(self):
        idx_name = 'autocomplete'
        self.create_auto_index(idx_name)
        with open('data/static/movies_cleaned.json', 'r') as j:
            contents = json.loads(j.read())
            for movie in contents:
                try:
                    self.elk_service.insert_document(idx_name, movie)
                except Exception as err:
                    continue
        print("Data inserted successfully for autocomplete.")
        return len(contents)
    
    def insert_tf_idf_data(self):
        idx_name = 'movies_tf_idf'
        self.create_tf_idf_index(idx_name)
        with open('data/static/movies_cleaned.json', 'r') as j:
            contents = json.loads(j.read())
            for movie in contents:
                try:
                    self.elk_service.insert_document(idx_name, movie)
                except Exception as err:
                    continue
        print("Data inserted for model Tf-Idf successfully.")
        return len(contents)
