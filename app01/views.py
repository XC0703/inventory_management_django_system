# 导入所需模块
import json
from app01.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# 注册功能
@csrf_exempt #处理跨域
def register(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中文不乱码，用json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    # print(reqBody)
    username = reqBody['userName']
    password = reqBody['userPassword']
    if username and password:
        # 判断字符串长度
        if len(username) > 15 or len(password) > 20:
            return JsonResponse({'code': -1, 'msg': '用户名或密码过长'})
        # 查找数据库中是否已经存在相同的userName
        user_name = User.objects.filter(userName=username)
        if user_name.exists():
            return JsonResponse({'code': -1, 'msg': '用户已存在'})
        # 如果不重复，在保存有关信息
        uesr_save = User(userName=username, userPassword=password)
        uesr_save.save()
        # 返回注册成功信息给前端
        return JsonResponse({'code': 0, 'msg': 'success'})
    else:
        return JsonResponse({'code': -1, "msg": "用户名或密码不能为空"})
