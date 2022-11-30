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
from django.contrib import admin
from django.urls import path
from app01 import views_order_cart
from app01 import views_user_ware

urlpatterns = [
    #添加订单
    path("miserorder/addOrder", views_order_cart.addOrder),
    #删除订单
    path("miserorder/deleteOrder", views_order_cart.deleteOrder),
    #查询单个订单
    path("miserorder/getOrder", views_order_cart.getOrder),
    #获取全部订单
    path("miserorder/getOrderlist", views_order_cart.getOrderlist),
    #添加临时订单
    path("misercart/addCart", views_order_cart.addCart),
    #删除临时订单
    path("misercart/deleteCart", views_order_cart.deleteCart),
    #编辑临时订单
    path("misercart/editCart", views_order_cart.editCart),
    #提交临时订单
    path("misercart/transCart",views_order_cart.transCart),
    #添加用户
    path("miseruser/addUser", views_user_ware.addUser),
    #删除用户
    path("miseruser/deleteUser", views_user_ware.deleteUser),
    #编辑用户
    path("miseruser/changeUser", views_user_ware.changeUser),
    #获取全部用户信息
    path("miseruser/getUserlist", views_user_ware.getUserlist),
    #获取单个用户信息
    path("miseruser/getUser", views_user_ware.getUser),
    #添加物品
    path("miserware/addWare", views_user_ware.addWare),
    #删除物品
    path("miserware/deleteWare", views_user_ware.deleteWare),
    #编辑物品
    path("miserware/changeWare", views_user_ware.changeWare),
    #获取物品清单
    path("miserware/getWarelist", views_user_ware.getWarelist),
    #查询单个物品
    path("miserware/getWare", views_user_ware.getWare),

]
