# searchapp/urls.py
from django.urls import path
from .views import search_view, search_view_live

urlpatterns = [
    path('search/', search_view, name='search'),
    path('live/', search_view_live, name='search_live'),

]
