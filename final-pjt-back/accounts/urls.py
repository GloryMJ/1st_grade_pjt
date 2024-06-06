from django.urls import path
from . import views

urlpatterns = [
    path('profileImageUpdate/<int:user_pk>/', views.updateProfile),
    path('profileInfoUpdate/<int:user_pk>/', views.updateInfo),
    path('profileLikeProducts/<int:user_pk>/', views.getLikeProducts),
    path('topProductsByAgeGroup/<int:age_group>/', views.getTopProductsByAgeGroup),
]