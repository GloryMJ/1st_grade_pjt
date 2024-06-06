from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
import requests
from django.conf import settings
from .models import Product, InfoProduct, Bank
from .serializers import ProductSerializer
from django.db.models import Count
from django.contrib.auth import get_user_model
from collections import defaultdict

@api_view(['GET'])
def top_products_by_age_group(request):
    User = get_user_model()
    age_groups = User.objects.values_list('age_group', flat=True).distinct()
    top_products_by_age_group = defaultdict(list)

    for age_group in age_groups:
        users_in_age_group = User.objects.filter(age_group=age_group)
        product_counts = defaultdict(int)

        for user in users_in_age_group:
            for product in user.like_products.all():
                product_counts[product] += 1

        sorted_products = sorted(product_counts.items(), key=lambda item: item[1], reverse=True)[:2]
        top_products_by_age_group[age_group] = [product[0] for product in sorted_products]

    # Serialize the data
    serialized_data = {}
    for age_group, products in top_products_by_age_group.items():
        serializer = ProductSerializer(products, many=True)
        serialized_data[age_group] = serializer.data

    return Response(serialized_data, status=status.HTTP_200_OK)



@api_view(['GET'])
def top_products(request):
    User = get_user_model()
    
    # 모든 유저들이 가장 좋아하는 상품 5개
    most_like_products = Product.objects.annotate(likes_count=Count('like')).order_by('-likes_count')[:5]
    most_like_products_serializer = ProductSerializer(most_like_products, many=True)
    
    # 연령대별 가장 많이 가입한 상품 2개
    age_groups = [10, 20, 30, 40, 50, 60, 70, 80]
    top_products_by_age_group = {}
    
    for age_group in age_groups:
        users_in_age_group = User.objects.filter(age_group=age_group)
        liked_products = Product.objects.filter(like__in=users_in_age_group)
        liked_products = liked_products.annotate(likes_count=Count('like')).order_by('-likes_count')[:2]
        top_products_by_age_group[age_group] = ProductSerializer(liked_products, many=True).data
    
    return Response({
        'most_like_products': most_like_products_serializer.data,
        'top_products_by_age_group': top_products_by_age_group
    })



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def deposit(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url)
    data = response.json()
    products = data.get('result', {}).get('baseList', [])
    detail_list = data.get('result', {}).get('optionList', [])

    new_products = []

    for item in products:
        fin_co_no = item.get('fin_co_no')
        bank, created = Bank.objects.get_or_create(
            fin_co_no=fin_co_no,
            defaults={'kor_co_nm': item.get('kor_co_nm')}
        )

        product_id = item.get('fin_prdt_cd')
        product, created = Product.objects.get_or_create(
            fin_prdt_cd=product_id,
            defaults={
                'bank': bank,
                'dcls_month': item.get('dcls_month'),
                'fin_prdt_nm': item.get('fin_prdt_nm'),
                'join_way': item.get('join_way'),
                'dcls_strt_day': item.get('dcls_strt_day'),
                'dcls_end_day': item.get('dcls_end_day'),
                'fin_co_subm_day': item.get('fin_co_subm_day'),
                # 예금관련 정보
                'mrtr_int': item.get('mrtr_int'),
                'spcl_cnd': item.get('spcl_cnd'),
                'join_deny': item.get('join_deny'),
                'join_member': item.get('join_member'),
                'etc_note': item.get('etc_note'),
                'max_limit': item.get('max_limit'),
                'bank_type': 1 # 예금상품
            }
        )

        if created:
            new_products.append(product)

        for detail in detail_list:
            if detail.get('fin_prdt_cd') == product_id:
                InfoProduct.objects.get_or_create(
                    product=product,
                    bank=bank,
                    defaults={
                        'intr_rate_type': detail.get('intr_rate_type', ''),
                        'intr_rate': detail.get('intr_rate', 0.0),
                        'intr_rate2': detail.get('intr_rate2', 0.0),
                        'save_trm': detail.get('save_trm', 0.0),
                        'spcl_cnd': detail.get('spcl_cnd', ''),
                        'rsrv_type': detail.get('rsrv_type', ''),
                    }
                )

    products = Product.objects.filter(bank_type=1)
    serializer = ProductSerializer(products, many=True)
    return Response({'message': 'Deposit data processed successfully', 'new_products': serializer.data})



# 적금 정보를 api에 요청 후, DB에 저장 / 있으면 패스
@api_view(['GET'])
def saving(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url)
    data = response.json()
    products = data.get('result', {}).get('baseList', [])
    detail_list = data.get('result', {}).get('optionList', [])

    new_products = []

    for item in products:
        fin_co_no = item.get('fin_co_no')
        bank, created = Bank.objects.get_or_create(
            fin_co_no=fin_co_no,
            defaults={'kor_co_nm': item.get('kor_co_nm')}
        )

        product_id = item.get('fin_prdt_cd')
        product, created = Product.objects.get_or_create(
            fin_prdt_cd=product_id,
            defaults={
                'bank': bank,
                'dcls_month': item.get('dcls_month'),
                'fin_prdt_nm': item.get('fin_prdt_nm'),
                'join_way': item.get('join_way'),
                'dcls_strt_day': item.get('dcls_strt_day'),
                'dcls_end_day': item.get('dcls_end_day'),
                'fin_co_subm_day': item.get('fin_co_subm_day'),
                # 적금관련 정보
                'mrtr_int': item.get('mrtr_int'),
                'spcl_cnd': item.get('spcl_cnd'),
                'join_deny': item.get('join_deny'),
                'join_member': item.get('join_member'),
                'etc_note': item.get('etc_note'),
                'max_limit': item.get('max_limit'),
                'bank_type': 2 # 예금상품
            }
        )

        if created:
            new_products.append(product)

        for detail in detail_list:
            if detail.get('fin_prdt_cd') == product_id:
                InfoProduct.objects.get_or_create(
                    product=product,
                    bank=bank,
                    defaults={
                        'intr_rate_type': detail.get('intr_rate_type', ''),
                        'intr_rate': detail.get('intr_rate', 0.0),
                        'intr_rate2': detail.get('intr_rate2', 0.0),
                        'save_trm': detail.get('save_trm', 0.0),
                        'spcl_cnd': detail.get('spcl_cnd', ''),
                        'rsrv_type': detail.get('rsrv_type', ''),
                    }
                )

    products = Product.objects.filter(bank_type=2)
    serializer = ProductSerializer(products, many=True)
    return Response({'message': 'Saving data processed successfully', 'new_products': serializer.data})




# # 주택담보대출 정보를 api 요청하고 DB에 저장, 있으면 패스
@api_view(['GET'])
def mortgage_loan(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url)
    data = response.json()
    products = data.get('result', {}).get('baseList', [])
    detail_list = data.get('result', {}).get('optionList', [])

    new_products = []

    for item in products:
        fin_co_no = item.get('fin_co_no')
        bank, created = Bank.objects.get_or_create(
            fin_co_no=fin_co_no,
            defaults={'kor_co_nm': item.get('kor_co_nm')}
        )

        product_id = item.get('fin_prdt_cd')
        product, created = Product.objects.get_or_create(
            fin_prdt_cd=product_id,
            defaults={
                'bank': bank,
                'dcls_month': item.get('dcls_month'),
                'fin_prdt_nm': item.get('fin_prdt_nm'),
                'join_way': item.get('join_way'),
                'dcls_strt_day': item.get('dcls_strt_day'),
                'dcls_end_day': item.get('dcls_end_day'),
                'fin_co_subm_day': item.get('fin_co_subm_day'),
                # 주택담보대출관련 정보
                'dly_rate': item.get('dly_rate'),
                'loan_lmt': item.get('loan_lmt'),
                'loan_inci_expn': item.get('loan_inci_expn'),
                'erly_rpay_fee': item.get('erly_rpay_fee'),
                'bank_type': 3 # 주택담보대출
            }
        )

        if created:
            new_products.append(product)

        for detail in detail_list:
            if detail.get('fin_prdt_cd') == product_id:
                InfoProduct.objects.get_or_create(
                    product=product,
                    bank=bank,
                    defaults={
                        'mrtg_type_nm': detail.get('mrtg_type_nm', ''),
                        'rpay_type_nm': detail.get('rpay_type_nm', ''),
                        'lend_rate_type_nm': detail.get('lend_rate_type_nm', ''),
                        'lend_rate_min': detail.get('lend_rate_min', ''),
                        'lend_rate_max': detail.get('lend_rate_max', '')
                    }
                )

    products = Product.objects.filter(bank_type=3)
    serializer = ProductSerializer(products, many=True)
    return Response({'message': 'Mortgage loan data processed successfully', 'new_products': serializer.data})



# 전세 대출 리스트를 API에 요청 후 저장, 없으면 
@api_view(['GET'])
def jeonse_loan(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url)
    data = response.json()
    products = data.get('result', {}).get('baseList', [])
    detail_list = data.get('result', {}).get('optionList', [])

    new_products = []

    for item in products:
        fin_co_no = item.get('fin_co_no')
        bank, created = Bank.objects.get_or_create(
            fin_co_no=fin_co_no,
            defaults={'kor_co_nm': item.get('kor_co_nm')}
        )

        product_id = item.get('fin_prdt_cd')
        product, created = Product.objects.get_or_create(
            fin_prdt_cd=product_id,
            defaults={
                'bank': bank,
                'dcls_month': item.get('dcls_month'),
                'fin_prdt_nm': item.get('fin_prdt_nm'),
                'join_way': item.get('join_way'),
                'dcls_strt_day': item.get('dcls_strt_day'),
                'dcls_end_day': item.get('dcls_end_day'),
                'fin_co_subm_day': item.get('fin_co_subm_day'),
                # 전세대출관련 정보
                'dly_rate': item.get('dly_rate'),
                'loan_lmt': item.get('loan_lmt'),
                'loan_inci_expn': item.get('loan_inci_expn'),
                'erly_rpay_fee': item.get('erly_rpay_fee'),
                'bank_type': 4 # 전세대출
            }
        )

        if created:
            new_products.append(product)

        for detail in detail_list:
            if detail.get('fin_prdt_cd') == product_id:
                InfoProduct.objects.get_or_create(
                    product=product,
                    bank=bank,
                    defaults={
                        'rpay_type_nm': detail.get('rpay_type_nm'),
                        'lend_rate_type_nm': detail.get('lend_rate_type_nm'),
                        'lend_rate_min': detail.get('lend_rate_min'),
                        'lend_rate_max': detail.get('lend_rate_max'),
                        'lend_rate_avg': detail.get('lend_rate_avg')
                    }
                )

    products = Product.objects.filter(bank_type=4)
    serializer = ProductSerializer(products, many=True)
    return Response({'message': 'Jeonse loan data processed successfully', 'new_products': serializer.data})



@api_view(['GET'])
def detail(request, product_pk):
    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def likes(request,product_pk):
    product = Product.objects.get(pk = product_pk)
    if request.method == 'PATCH':
        if request.user in product.like_users.all():
            product.like_users.remove(request.user)
            return Response({'result' : 'remove'}, status=status.HTTP_202_ACCEPTED)
        else:
            product.like_users.add(request.user)
            return Response({'result' : 'add'}, status=status.HTTP_202_ACCEPTED)