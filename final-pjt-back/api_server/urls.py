from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from ..accounts import views as accountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')), #REST_AUTH
    path('accounts/signup/', include('dj_rest_auth.registration.urls')), #REST_AUTH
    path('accounts/update/', include('accounts.urls')), #REST_AUTH
    path('articles/', include('articles.urls')),
    path('products/', include('products.urls')),
    path('subscribe/', include('subscribe.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Media 링크 셋팅
