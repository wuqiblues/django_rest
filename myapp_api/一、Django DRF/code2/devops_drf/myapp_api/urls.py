from django.urls import path, include, re_path
from myapp_api import views

urlpatterns = [
    re_path('api/user/$', views.UserView.as_view()),
    re_path('api/user/(?P<pk>\d+)/$', views.UserView.as_view()),
    re_path('api/project/$', views.ProjectView.as_view()),
    re_path('api/app/$', views.AppView.as_view()),
    re_path('api/server/$', views.ServerView.as_view()),
    re_path('api/test/$', views.TestView.as_view()),
    re_path('api/test/(?P<id>\d+)/$', views.TestView.as_view()),
    # re_path('api/test2/$', views.Test2View.as_view({'get': 'list', 'post': 'create','delete': 'destory','put': 'update',})),
    # re_path('api/test2/(?P<pk>\d+)/$', views.Test2View.as_view({'get': 'retrieve'})),
]

from rest_framework import routers

router = routers.DefaultRouter() # 定义路由实例
router.register(r'test2', views.Test2View, basename='test2') # 注册一个路由

urlpatterns += [
    path('api/', include(router.urls))  # myapp_api/api/test2
]
