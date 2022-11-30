import requests
import pandas as pd
from search import settings


class RetriveResults:
    def __init__(self):
        self.BASE_URL = f'{settings.BACKEND_BASE_URL}/api/search'
    
    def get_results_by_BM25(self,request):
        url = f'{self.BASE_URL}/search_text_field_bm25'
        data = requests.get(url, data=request)
        results = data.json()
        return results
