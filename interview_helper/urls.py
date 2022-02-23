from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('faqs/', views.faqspage, name='faqs'),
    path('overview/', views.overviewpage, name='overview'),
]