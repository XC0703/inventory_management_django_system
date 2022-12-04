from django.shortcuts import render

# Create your views here.
# 导⼊所需模块
import json
from app.models import *
# 处理跨域
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse


# 临时订单添加
@csrf_exempt  # 处理跨域
def addCart(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    print(reqBody)
    try:
        ware_id = reqBody['wareId']
        ware_count = reqBody['wareCount']
        warefilter = Ware.objects.filter(wareId=ware_id)
        if warefilter.exists():
            ware = json.loads(serializers.serialize("json", warefilter))[0]
            warecount_ori = int((ware['fields'])['wareCount'])
            warecount_fin = warecount_ori - ware_count
            if warecount_fin < 0:
                return JsonResponse({'code': -1, 'msg': '库存物品数量不足'})
            else:
                order_save = Cart(userId=reqBody['userId'],
                                  userName=reqBody['userName'],
                                  wareCount=reqBody['wareCount'],
                                  wareId=reqBody['wareId'],
                                  wareName=reqBody['wareName'])
                order_save.save()
                return JsonResponse({'code': 0, 'msg': 'success'})
        else:
            return JsonResponse({'code': -1, 'msg': '该物品不存在'})
    # 防止异常处理太过宽泛
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '临时订单添加失败'})


# 临时订单删除
@csrf_exempt  # 处理跨域
def deleteCart(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    # print(reqBody)
    try:
        for cartid in reqBody:
            print(cartid)
            cart_id = Cart.objects.filter(cartId=cartid)
            print(cart_id)
            # exists = models.Order.objects.exists(orderId=orderId).exists()
            if not cart_id.exists():
                return JsonResponse({'code': -1, 'msg': '删除失败，数据不存在', '错误发生id': cart_id})
            else:
                Cart.objects.filter(cartId=cartid).delete()
        return JsonResponse({'code': 0, 'msg': 'success'})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '临时订单删除失败'})


# 编辑临时订单
@csrf_exempt  # 处理跨域
def updateCart(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    try:
        cartId = reqBody['cartId']
        wareCount = reqBody['wareCount']
        row_object = Cart.objects.filter(cartId=cartId)
        if not row_object.exists():
            return JsonResponse({"code": -1, 'msg': "数据不存在，请刷新重试"})
        else:
            row_object.update(wareCount=wareCount)
        # form = CartModelForm(data=request.POST, instance=row_object)
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse({"status": True})
        return JsonResponse({"code": 0, 'msg': 'success'})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '临时订单编辑失败'})


# 查询全部临时订单,获取用户权限，高于100才能获取全部
@csrf_exempt  # 处理跨域
def getCartlist(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    # reqBody = json.loads(request.body.decode())
    try:
        userInfo = request.session.get('userInfo', None)
        if userInfo:
            user = userInfo["fields"]
            power = int(user["userPower"])
            if power > 100:
                qs = Cart.objects.values()
                # 将QuerySet对象转化为list类型
                # 否则不能被转化为JSON字符串
                retlist = list(qs)
                return JsonResponse({'code': 0, 'msg': 'success', 'line': '全部临时订单', 'cartList': retlist})
            else:
                # return JsonResponse({'code': -1, 'msg': '用户权限不足'})
                userid = user["userId"]
                qs = Cart.objects.filter(userId=userid).values()
                retlist = list(qs)
                return JsonResponse({'code': 0, 'msg': 'success', 'line': '权限不足，仅显示个人负责的临时订单', 'cartList': retlist})
        else:
            return JsonResponse({'code': -1, "msg": "未查找到登录信息"})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取订单信息失败'})


# 临时订单提交（删除临时订单，数据添加到订单，并更改物品数量)
@csrf_exempt  # 处理跨域
def transCart(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    try:
        fail_ware_ids = []
        for cartInfo in reqBody:
            ware_id = cartInfo['wareId']
            ware_count = cartInfo['wareCount']
            warecount_ori = Ware.objects.get(wareId=ware_id).wareCount
            warecount_fin = warecount_ori - ware_count
            if warecount_fin < 0:
                fail_ware_ids.append(ware_id)
                # print(fail_ware_ids)
                # return JsonResponse({'code': -1, 'msg': '库存物品数量不足'})
            else:
                # 改变库存中对应物品的数量
                row_object = Ware.objects.filter(wareId=ware_id)
                row_object.update(wareCount=warecount_fin)
                # 将临时订单添加到订单
                order_save = Order(userId=cartInfo['userId'],
                                   userName=cartInfo['userName'],
                                   wareCount=cartInfo['wareCount'],
                                   wareId=cartInfo['wareId'],
                                   wareName=cartInfo['wareName'])
                order_save.save()
                # print("success")
                # 添加完成后删除该临时订单
                cart_id = cartInfo['cartId']
                Cart.objects.filter(cartId=cart_id).delete()
                # print("success")
        # print(len(fail_ware_ids))
        if len(fail_ware_ids) == 0:
            return JsonResponse({"code": 0, 'msg': 'success'})
        else:
            return JsonResponse({'code': -1, 'msg': '库存物品数量不足', 'fail_ware_ids': fail_ware_ids})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '临时订单提交失败'})

