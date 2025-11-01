from rest_framework import viewsets, generics
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [IsAuthenticated]