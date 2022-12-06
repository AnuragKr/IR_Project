from django.urls import path
from . import views

urlpatterns = [
    path('search_text_bm25', views.get_bm25_text_result),
    path('search_text_field_bm25', views.get_field_search_result),
    path('search_text_tf_idf', views.get_tf_idf_text_result),
    path('search_text', views.get_text_result),
    path('search_fuzzy_text_bm25', views.get_bm25_fuzzy_text_result),
    path('get_suggestion_bm25', views.get_bm25_search_suggestion),
    path('get_phrase_bm25', views.get_phrase_text_result),

]
