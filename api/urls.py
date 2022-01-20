from django.urls import path
from .views import home, is_match #template

urlpatterns = [
    path('', home),
    path('api/is_match/', is_match),
]