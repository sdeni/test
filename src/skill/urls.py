from django.urls import path, re_path
from django.views.generic import TemplateView
from .Controllers.Home import home
from .Controllers.Auth import auth

from .views import (
    PostDetailAPIView,
    PostListCreateAPIView,
)

app_name = 'skill-api'
urlpatterns = [
    path('', home.index),
    path('list/', PostListCreateAPIView.as_view(), name='list-create'),
    path('', PostListCreateAPIView.as_view(), name='list-create'),
    path('logout/', auth.logout_view, name="logout"),
    path('login/', auth.login_view, name="login"),
    path('registration/', auth.MyRegisterFormView.as_view(), name="register"),
    path('login/enter/', auth.enter, name="enter"),
    path('react/', TemplateView.as_view(template_name='react.html')),
    re_path(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),

]
