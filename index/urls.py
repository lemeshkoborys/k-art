from django.urls import path
from .views import render_index


urlpatterns = [
    path('', render_index, name='index')
]