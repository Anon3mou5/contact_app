from .views import Contact
from django.urls import  path,include
from rest_framework.routers import  DefaultRouter
router = DefaultRouter()
router.register(r'users', Contact)
urlpatterns = [
    path(r'',include(router.urls))
]