from rest_framework.viewsets import ModelViewSet
from .models import Blog
from .serializers import Blog_Serializer
from rest_framework.permissions import AllowAny

class BlogView(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=Blog_Serializer
    permission_classes=[AllowAny]