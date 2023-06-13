
from django.urls import path, include
from myapp import views

urlpatterns = [
    # path('user/', views.user),
    path('user/', views.UserView.as_view()),  # 类视图
    path('user_list', views.user_list),
    path('user_add', views.user_add),
    path('user_edit', views.user_edit),
]