from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserProfileImageSerializer, UserProfileUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from products.models import Product 
from products.serializers import ProductSerializer  



@api_view(['POST'])
def updateProfile(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk = user_pk)
    serializer = UserProfileImageSerializer(instance=person, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
@api_view(['PATCH'])
def updateInfo(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk = user_pk)
    serializer = UserProfileUpdateSerializer(instance=person, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLikeProducts(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    liked_products = user.like_products.all()  # User가 좋아요한 상품 목록
    serializer = ProductSerializer(liked_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getTopProductsByAgeGroup(request, age_group):
    User = get_user_model()
    users_in_age_group = User.objects.filter(age_group=age_group)
    product_counts = {}

    for user in users_in_age_group:
        for product in user.like_products.all():
            if product in product_counts:
                product_counts[product] += 1
            else:
                product_counts[product] = 1

    sorted_products = sorted(product_counts.items(), key=lambda item: item[1], reverse=True)[:5]
    top_products = [product[0] for product in sorted_products]
    serializer = ProductSerializer(top_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)