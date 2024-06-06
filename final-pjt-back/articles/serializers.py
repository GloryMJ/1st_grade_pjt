from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    nickname= serializers.CharField(source = "user.nickname", read_only=True)
    class Meta:
        model = Article
        fields = ('pk', 'nickname', 'title', 'article_type', 'views')
        
class CommentSerializer(serializers.ModelSerializer):
    nickname= serializers.CharField(source = "user.nickname", read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'article']
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many = True, read_only = True)
    nickname= serializers.CharField(source = "user.nickname", read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['user', 'nickname' , 'created_at', 'views']

