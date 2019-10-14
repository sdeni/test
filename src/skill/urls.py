from django.urls import path, re_path, include
from django.views.generic import TemplateView
from .Controllers.Home import home
from .Controllers.Auth import auth
from .Controllers.Payment import payment
from .Controllers.Catalog import catalog

from .views import (
    PostDetailAPIView,
    PostListCreateAPIView,
)

# app_name = 'skill-api'
urlpatterns = [
    path('', home.index),
    path('list/', PostListCreateAPIView.as_view(), name='list-create'),
    path('signup/', auth.signup, name='signup'),
    path('signup/', include('social_django.urls', namespace='social')),
    path('signin/', auth.signin, name='signin'),
    path('signin/', include('social_django.urls', namespace='social')),
    path('logout/', auth.exit, name='logout'),
    path('forgot/', auth.forgot, name='forgot'),
    path('activate/<uidb64>/<token>/', auth.activate, name='activate'),
    path('react/', TemplateView.as_view(template_name='react.html')),
    path('react/payment/', TemplateView.as_view(template_name='react.html')),
    path('catalog/', catalog.show, name='catalog'),
    path('payment/', payment.view, name='initial'),
    re_path(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
]
