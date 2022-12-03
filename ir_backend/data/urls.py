from django.urls import path
from . import views

urlpatterns = [
    path('insert', views.insert_data),
    path('insert/tf_idf', views.insert_tf_idf_data),
    path('insert/autosuggestion', views.insert_auto_suggestion_data),
]
