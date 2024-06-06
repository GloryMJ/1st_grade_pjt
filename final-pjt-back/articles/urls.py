from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.article_list),
    path('post/', views.article_post),
    path('<int:article_id>/detail/', views.article_detail),
    path('<int:article_id>/put/', views.article_put),
    path('<int:article_id>/delete/', views.article_delete),
    path('<int:article_id>/comments/', views.comments),
    path('<int:article_id>/comments/<int:comment_id>/', views.comment_delete),
]
