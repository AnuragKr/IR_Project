import requests
import pandas as pd
from search import settings
import json


class RetriveResults:
    def __init__(self):
        self.BASE_URL = f'{settings.BACKEND_BASE_URL}/api/search'
    
    def get_results_by_BM25(self,request):
        url = f'{self.BASE_URL}/search_text_bm25'
        data = requests.get(url, data=request)
        results = data.json()
        return results

    def get_auto_suggetions(self,request):
        url = f'{self.BASE_URL}/get_suggestion_bm25'
        data = requests.get(url, data=request)
        results = data.json()
        return results

    def get_results_by_field_query(self, request):
        url = f'{self.BASE_URL}/search_text'
        print(url, request)
        headers = {'content-type': 'application/json'}
        data = requests.get(url, data=json.dumps(request), headers=headers)
        # data = requests.get(url, data=request)
        results = data.json()
        return results

