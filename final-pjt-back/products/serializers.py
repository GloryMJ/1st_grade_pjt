from rest_framework import serializers
from .models import Bank, Product, InfoProduct

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class InfoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    infoproducts = InfoProductSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source = "like_users.count", read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
