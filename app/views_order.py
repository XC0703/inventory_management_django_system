from django.shortcuts import render

# Create your views here.
# 导⼊所需模块
import json
from app.models import *
# 处理跨域
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# 订单添加
@csrf_exempt  # 处理跨域
def addOrder(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    try:
        '''更改物品数量'''
        # 改变库存中对应物品的数量
        ware_id = reqBody['wareId']
        ware_count = reqBody['wareCount']
        ware_name = reqBody['wareName']
        warecount_ori = Ware.objects.get(wareId=ware_id).wareCount
        warecount_fin = warecount_ori - ware_count
        warename_ori = Ware.objects.get(wareId=ware_id).wareName

        if ware_name != warename_ori:
            return JsonResponse({'code': -1, 'msg': '物品编号和物品名不匹配'})
        elif warecount_fin < 0:
            return JsonResponse({'code': -1, 'msg': '库存物品数量不足'})
        else:
            row_object = Ware.objects.filter(wareId=ware_id)
            row_object.update(wareCount=warecount_fin)
            '''物品数量更新后添加订单记录'''
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
                return JsonResponse({'code': -1, 'msg': '删除失败，数据不存在', '错误发生id': order_id})
            else:
                Order.objects.filter(orderId=orderid).delete()
        return JsonResponse({'code': 0, 'msg': 'success'})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '订单删除失败'})


# 查询全部订单
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
        return JsonResponse({'code': 0, 'msg': 'success', 'orderList': retlist})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取订单信息失败'})


# 查询单个订单
@csrf_exempt  # 处理跨域
def getOrder(request, theme):
    # return HttpResponse(theme)
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    orderid = theme
    order_id_info = Order.objects.filter(orderId=orderid).values()
    order_id = Order.objects.filter(orderId=orderid)
    # print(order_id_info)
    # exists = models.Order.objects.exists(orderId=orderId).exists()
    if not order_id.exists():
        return JsonResponse({'code': -1, 'msg': '该订单信息不存在'})
    try:
        order_info = list(order_id_info)[0]
        return JsonResponse({'code': 0, 'msg': 'success', 'orderInfo': order_info})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取订单信息失败'})

