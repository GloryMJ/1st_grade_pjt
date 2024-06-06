from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article, Comment
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CommentSerializer
from .models import Article, Comment
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
User = get_user_model()
# Create your views here.

@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PATCH'])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        article.views += 1
        article.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def article_put(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    if request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def article_delete(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_post(request):
    if request.method == 'POST':
        serializer = ArticleDetailSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comments(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    if request.method == 'POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user, article = article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

