from django.urls import path, include
from rest_framework import routers
from .views import home, is_match, test #template

router = routers.DefaultRouter()
router.register(r'is_match')

urlpatterns = [
    path('', home),
    path('api/is_match/', is_match),
    path('api/test/', test)
]