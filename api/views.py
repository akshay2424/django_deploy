from rest_framework import viewsets, generics
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]