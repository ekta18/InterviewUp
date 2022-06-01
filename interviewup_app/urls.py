from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('faqs/', views.faqspage, name='faqs'),
    path('news/', views.newspage, name='news'),
    path('overview/', views.overviewpage, name='overview'),
    path('resume/', views.showfile, name='resumeinput'),
    path('videos/', views.experiencevideospage, name='experiencevideos'),
    path('domain/', views.domainpage, name='domain')

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)