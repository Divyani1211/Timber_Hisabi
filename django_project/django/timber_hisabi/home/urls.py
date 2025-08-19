from django.urls import path
from.import views
urlpatterns=[
    path('',views.home_page,name='home'),
     path('', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('home/', views.home_view, name="home"),
]