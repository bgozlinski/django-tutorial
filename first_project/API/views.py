from rest_framework.viewsets import generics
from .serializers import ArticleSerializer
from blog.models import Article
from rest_framework.permissions import IsAuthenticated

class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class GetArticle(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article


class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

