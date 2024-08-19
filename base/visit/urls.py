from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="homepage"),
    path('video/', views.video, name="video"),
    path('faq/', views.faq, name="faq"),
    path('blog/', views.blog, name="blog"),
    path('opinions/', views.opinions, name="opinions"),
    path('login/', views.login, name="login"),
    path('adminmain/', views.adminmain, name="adminmain"),
    path('elevator/', views.elevator, name="elevator"),
    # path('logout/', views.user_logout, name="logout"),


    # path('test/', views.test, name="test"),
]
