from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('created_urls/', views.UrlListView.as_view(), name='created_urls'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<slug:shortcode>/', views.ShortenerView.as_view(), name='scode'),
]
