from django.shortcuts import render

# Create your views here.
# 导⼊所需模块
import json
from app01.models import *
# 处理跨域
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render


# 订单增加
# lHlluffy
@csrf_exempt  # 处理跨域
def addOrder(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    try:
        order_save = Order(userId=reqBody['userId'],
                           userName=reqBody['userName'],
                           wareCount=reqBody['wareCount'],
                           wareId=reqBody['wareId'],
                           wareName=reqBody['wareName'])
        order_save.save()
        return JsonResponse({'code': 0, 'msg': 'success'})
    # 防止异常处理太过宽泛
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '订单添加失败'})


# 订单删除
# lHlluffy
@csrf_exempt  # 处理跨域
def deleteOrder(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    print(reqBody)
    try:
        for orderid in reqBody:
            print(orderid)
            order_id = Order.objects.filter(orderId=orderid)
            # exists = models.Order.objects.exists(orderId=orderId).exists()
            if not order_id.exists():
                return JsonResponse({'code': -1, 'msg': '删除失败，数据不存在'})
            else:
                Order.objects.filter(orderId=orderid).delete()
                return JsonResponse({'code': 0, 'msg': 'success'})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '订单删除失败'})


# 查询全部订单
# lHlluffy
@csrf_exempt  # 处理跨域
def getOrderlist(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    # reqBody = json.loads(request.body.decode())
    qs = Order.objects.values()
    try:
        # 将QuerySet对象转化为list类型
        # 否则不能被转化为JSON字符串
        retlist = list(qs)
        return JsonResponse({'code': 0, 'msg': 'success', 'retlist': retlist})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取订单信息失败'})


# 查询单个订单
# lHlluffy
@csrf_exempt  # 处理跨域
def getOrder(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    print(reqBody)
    order_id = Order.objects.filter(orderId=reqBody).values()
    try:
        order_info = list(order_id)
        return JsonResponse({'code': 0, 'msg': 'success', 'orderinfo': order_info})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取订单信息失败'})