from django.urls import path
from .views import post_detail

urlpatterns = [
    path('post/', post_detail, name='post_detail'),
]
