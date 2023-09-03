from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogView
router=DefaultRouter()
router.register('blogs',BlogView,basename='blogs')
urlpatterns=[]+router.urls
