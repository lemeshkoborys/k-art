from django.urls import path
from .views import render_contacts_page, feedback

urlpatterns = [
    path('', render_contacts_page, name='contacts'),
    path('feedback/', feedback, name='feedback')
]
