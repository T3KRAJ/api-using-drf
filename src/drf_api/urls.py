from core.views import TestView
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
  