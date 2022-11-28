from django.urls import path
from . import views

urlpatterns = [
    path('search_text_field_bm25', views.get_bm25_text_field_result),
]
