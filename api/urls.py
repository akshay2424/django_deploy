from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterViewSet.as_view(), name='register'),
]
