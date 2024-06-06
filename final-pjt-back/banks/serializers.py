from rest_framework import serializers
from .models import ExchangeRate, Bank, Product, LikeProduct, InfoProduct, ReviewComment


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
        

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LikeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields = '__all__'
        read_only_fields = ['product', 'bank', 'user']

class InfoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = '__all__'
        read_only_fields = ['product', 'bank']

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ['user', 'product', 'created_at']