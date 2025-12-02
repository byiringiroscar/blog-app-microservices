import requests
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

USER_SERVICE_URL = "http://127.0.0.1:8000/api/users/" 

# Create your views here.

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def create(self, request, *args, **kwargs):
        author_id = request.data.get('author_id')
        # Validate user exists in User Service
        try:
            response = requests.get(f"{USER_SERVICE_URL}{author_id}/")
            if response.status_code != 200:
                return Response({"error": "Author not found"}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.ConnectionError:
            return Response({"error": "Cannot connect to User Service"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return super().create(request, *args, **kwargs)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer