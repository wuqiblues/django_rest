
from django.urls import path, include
from myapp_api import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # 类视图
]