from django.db import models
from django.conf import settings

class Bank(models.Model):
    bank_pk = models.AutoField(primary_key=True)
    fin_co_no = models.CharField(max_length=20, unique=True)    # 금융회사코드
    kor_co_nm = models.CharField(max_length=255)                # 금융회사이름

    def __str__(self):
        return self.kor_co_nm

class Product(models.Model):
    # 상품 공통 필드
    product_pk = models.AutoField(primary_key=True)                     # 기본 키로 설정
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)            # 필드 이름 수정
    dcls_month = models.TextField()                                     # 공시제출월
    fin_prdt_cd = models.CharField(max_length=20, unique=True)          # 금융상품코드
    fin_prdt_nm = models.CharField(max_length=255)                      # 금융상품이름
    join_way = models.TextField()                                       # 가입방법
    dcls_strt_day = models.TextField(null=True, blank=True)             # 공시시작일
    dcls_end_day = models.TextField(null=True, blank=True)              # 공시 종료일
    fin_co_subm_day = models.TextField(null=True, blank=True)           # 금융회사 제출일

    # 예적금 관련
    mrtr_int = models.TextField(null=True, blank=True)                  # 만기 후 이자율
    spcl_cnd = models.TextField(null=True, blank=True)                  # 우대조건
    join_deny = models.TextField(null=True, blank=True)                 # 가입제한 / 1: 제한 없음, 2: 서민전용, 3: 일부제한 
    join_member = models.TextField(null=True, blank=True)               # 가입대상
    etc_note = models.TextField(null=True, blank=True)                  # 기타유의사항
    max_limit = models.IntegerField(null=True, blank=True)              # 최고한도

    # 대출 관련
    dly_rate = models.CharField(max_length=100, null=True, blank=True)  # 연체이자율
    loan_lmt = models.CharField(max_length=100, null=True, blank=True)  # 대출한도
    loan_inci_expn = models.TextField(null=True, blank=True)            # 대출부대비용
    erly_rpay_fee = models.TextField(null=True, blank=True)             # 중도상환수수료

    bank_type = models.IntegerField(choices=[                           # 상품종류
        (1, '예금상품'),
        (2, '적금상품'),
        (3, '주택담보대출'),
        (4, '전세대출'),
    ])
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_products')

    def __str__(self):
        return self.fin_prdt_nm

class InfoProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='infoproducts')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)   # 필드 이름 수정

    # 예적금 정보
    
    intr_rate_type = models.TextField(null=True, blank=True)    # 저축금리유형 / 단리:S, 복리:M
    intr_rate = models.FloatField(null=True, blank=True)        # 저축금리 / 개월
    intr_rate2 = models.FloatField(null=True, blank=True)       # 우대금리 / 개월
    save_trm = models.FloatField(null=True, blank=True)         # 저축기간 / 개월
    spcl_cnd = models.TextField(null=True, blank=True)          # 우대조건
    rsrv_type = models.TextField(null=True, blank=True)         # 적립유형 / 정액적립식, 자유적립식

    # 대출 정보    
    mrtg_type_nm = models.TextField(null=True, blank=True)      # 담보유형 / 아파트, 아파트 외
    rpay_type_nm = models.TextField(null=True, blank=True)      # 대출상환유형 / 분할상환방식, 만기일시상환방식
    lend_rate_type_nm = models.TextField(null=True, blank=True) # 대출금리유형 / 고정금리, 변동금리
    lend_rate_min = models.TextField(null=True, blank=True)     # 대출금리 최저
    lend_rate_max = models.TextField(null=True, blank=True)     # 대출금리 최고
    lend_rate_avg = models.TextField(null=True, blank=True)     # 전월취급평균금리


