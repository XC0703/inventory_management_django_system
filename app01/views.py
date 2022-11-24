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