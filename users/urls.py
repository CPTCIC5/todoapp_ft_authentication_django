from django.urls import path
from . import views
from django.contrib.auth import views as cbv_views

app_name='users'

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',cbv_views.LoginView.as_view(template_name='users/login.html'),name='login'),   
    path('logout/',cbv_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('acc_del/<int:acc>/',views.acc_del,name='acc_del')
]