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
from app01 import views_user
from app01 import views_ware

# 注册路由
urlpatterns = [
    #增加用户
    path("miseruser/addUser", views_user.addUser),
    #删除用户
    path("miseruser/deleteUser", views_user.deleteUser),
    #更改用户
    path("miseruser/changeUser", views_user.changeUser),
    #查询全部用户
    path("miseruser/getUserlist", views_user.getUserlist),
    #查询单个用户
    path("miseruser/getUser/<theme>", views_user.getUser, name='userid'),
    #新增库存
    path("miserware/addware", views_ware.addware),
    #删除库存
    path("miserware/deleteWare", views_ware.deleteWare),
    #更改库存
    path("miserware/changeWare", views_ware.changeWare),
    #查询全部库存
    path("miserware/getWarelist", views_ware.getWarelist),
    #查询单个库存
    path("miserware/getWare/<theme>", views_ware.getWare, name='wareid'),
]

