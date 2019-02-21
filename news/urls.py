from django.urls import path
from .views import render_news, render_new_detail

urlpatterns = [
    path('', render_news, name='new-list'),
    path('<int:pk>/detail/', render_new_detail, name='new-detail')
]