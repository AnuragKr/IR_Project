from django.urls import path
from . import views

urlpatterns = [
    path('search_text_bm25', views.get_bm25_text_result),
    path('search_fuzzy_text_bm25', views.get_bm25_fuzzy_text_result),
    path('get_suggestion_bm25', views.get_bm25_search_suggestion),
]