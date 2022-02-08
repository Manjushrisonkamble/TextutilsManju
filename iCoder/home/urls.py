from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('authors/<int:authorName>', views.authors, name="Authors"),
    path('sum/<int:x>/<int:y>', views.sum, name="sum"),
    path('<int:x>/<str:y>', views.concat, name="concat"),
    path('search/', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]