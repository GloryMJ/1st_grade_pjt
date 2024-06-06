from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class ExchangeRate(models.Model):
    # 국가코드
    cur_unit = models.TextField()
    # 국가 / 통화명
    cur_num = models.TextField()
    # 받을 때
    ttb = models.IntegerField(default=0)
    # 보낼 때
    tts = models.IntegerField(default=0)

class Bank(models.Model):
    # 금융 상품 코드
    fin_co_no = models.TextField()
    # 금융 회사 코드
    kor_co_no = models.TextField()

class Product(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='products')
    dcls_month = models.DateField()
    fin_prdt_cd = models.TextField(unique=True)
    fin_prdt_nm = models.TextField()
    join_way = models.TextField()
    back_type = models.IntegerField()
    
class LikeProduct(models.Model):
    product = models.ManyToManyField(Product, related_name='liked_products')
    bank = models.ManyToManyField(Bank, related_name='liked_products')
    user = models.ManyToManyField(User, related_name='liked_products')
    
class InfoProduct(models.Model):
    # 상품키
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='info_products')
    # 은행키
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='info_products')
    # 가입제한
    join_deny = models.TextField(blank=True, null=True)
    # 기타유의사항
    etc_note = models.TextField(blank=True, null=True)
    # 저축금리유형    
    intr_rate_type = models.CharField(max_length=10, choices=[('S', '단리'), ('M', '복리')], default='S',)
    # 저축금리
    intr_rate = models.FloatField(blank=True, null=True)
    # 우대금리
    intr_rate2 = models.FloatField(blank=True, null=True)
    # 저축기간(개월)
    save_trm = models.IntegerField(blank=True, null=True)
    # 우대조건
    spcl_cnd = models.TextField(blank=True, null=True)
    # 적립유형
    rsrv_type = models.TextField(blank=True, null=True)
    # 대출부대비용
    loan_inci_expn = models.TextField(blank=True, null=True)
    # 중도상환수수료
    erly_rpay_fee = models.TextField(blank=True, null=True)
    # 연체이자율
    dly_rate = models.TextField(blank=True, null=True)
    # 대출상환유형
    rpay_type_nm = models.TextField(blank=True, null=True)
    # 대출금리유형
    lend_rate_type_nm = models.TextField(blank=True, null=True)
    # 대출금리최저
    lend_rate_min = models.FloatField(blank=True, null=True)
    # 대출금리최고
    lend_rate_max = models.FloatField(blank=True, null=True)
    # 전월취급 평균금리
    lend_rate_avg = models.FloatField(blank=True, null=True)
    
class ReviewComment(models.Model):
    # 댓글
    content = models.TextField()
    product = models.ManyToManyField(Product, related_name='review_comments')
    user = models.ManyToManyField(User, related_name='review_comments')