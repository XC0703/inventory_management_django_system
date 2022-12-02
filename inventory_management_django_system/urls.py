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
from app import views_auth, views_ware, views_user, views_sales, views_order, views_cart

# 注册路由
urlpatterns = [
    # 库存管理模块--miserware
    # 新增库存
    path("miserware/addware", views_ware.addware),
    # 删除库存
    path("miserware/deleteWare", views_ware.deleteWare),
    # 更改库存
    path("miserware/updateWare", views_ware.updateWare),
    # 获取物品清单
    path("miserware/getWarelist", views_ware.getWarelist),
    # 获取单个物品信息
    path("miserware/getWare/<theme>", views_ware.getWare, name='wareid'),


    # 用户管理模块--miseruser
    # 增加用户
    path("miseruser/addUser", views_user.addUser),
    # 删除用户
    path("miseruser/deleteUser", views_user.deleteUser),
    # 更改用户
    path("miseruser/updateUser", views_user.updateUser),
    # 获取用户信息清单
    path("miseruser/getUserlist", views_user.getUserlist),
    # 获取单个用户信息
    path("miseruser/getUser/<theme>", views_user.getUser, name='userid'),


    # 订单管理模块--miserorder
    # 添加订单
    path("miserorder/addOrder", views_order.addOrder),
    # 删除订单
    path("miserorder/deleteOrder", views_order.deleteOrder),
    # 查询单个订单
    path("miserorder/getOrder/<theme>", views_order.getOrder, name='orderid'),
    # 获取全部订单
    path("miserorder/getOrderlist", views_order.getOrderlist),


    # 临时订单模块--misercart
    # 添加临时订单
    path("misercart/addCart", views_cart.addCart),
    # 删除临时订单
    path("misercart/deleteCart", views_cart.deleteCart),
    # 编辑临时订单
    path("misercart/editCart", views_cart.editCart),
    # 查询临时订单,需要判断用户权限，高于100才能获取全部
    path("misercart/getCartlist", views_cart.getCartlist),
    # 提交临时订单
    path("misercart/transCart", views_cart.transCart),


    # 登录注册模块--miserauth
    # 注册功能
    path("miserauth/register", views_auth.userRegister),
    # 登录功能
    path("miserauth/login", views_auth.userLogin),
    # 获取当前登录信息
    path("miserauth/getloginUser", views_auth.getLoginUser),
    # 退出登录
    path("miserauth/loginout", views_auth.loginOut),


    # 数据可视化模块--misersales
    # 将销售数据传入数据库
    path("misersales/saveSalesData", views_sales.saveSalesData),
    # 获取数据库中的销售数据
    path("misersales/getSalesData", views_sales.getSalesData)
]
