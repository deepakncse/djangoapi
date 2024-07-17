from . import views
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', views.CourseView)
urlpatterns = [
 path('',include(router.urls))  
]
