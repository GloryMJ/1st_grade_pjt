from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('deposit/', views.deposit),
    path('saving/', views.saving),
    path('mortgage_loan/', views.mortgage_loan),
    path('jeonse_loan/', views.jeonse_loan),
    path('all/', include(router.urls)),
    path('<int:product_pk>/detail/', views.detail),
    path('<int:product_pk>/likes/', views.likes),
    path('topProductsByAgeGroup/', views.top_products_by_age_group),
]
