from django.urls import path
from .views import qa_view

urlpatterns = [
    path('', qa_view, name='qa')
]