from django.urls import path, include, re_path
from myapp_api import views

urlpatterns = [
    re_path('api/user/$', views.UserView.as_view()),
    re_path('api/user/(?P<pk>\d+)/$', views.UserView.as_view()),
    re_path('api/project/$', views.ProjectView.as_view()),
    re_path('api/app/$', views.AppView.as_view()),
    re_path('api/server/$', views.ServerView.as_view()),
]