from django.urls import path
from . import views

urlpatterns = [
    path('insert', views.insert_data),
    path('insert/autosuggestion', views.insert_auto_suggestion_data),
]
