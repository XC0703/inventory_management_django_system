"""inventory_management_django_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 导入所需模块
from django.urls import path
from app01 import views

# 注册路由
urlpatterns = [
    path("miserauth/register", views.userRegister),
    path("miserauth/login", views.userLogin),
    path("miserauth/getloginUser", views.getLoginUser),
    path("miserauth/loginout", views.loginOut),
]
