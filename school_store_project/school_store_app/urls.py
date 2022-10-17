from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
   # path('user_registration/<int:id>/', views.user_registration, name="user_registration")
]
