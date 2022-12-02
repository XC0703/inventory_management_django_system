# 导入所需模块
from app.models import *
# 处理跨域
from django.views.decorators.csrf import csrf_exempt
# JSON对象序列化
import json
from django.core import serializers
from django.http import JsonResponse
# 防止重复登录
from django.contrib.sessions.models import Session
from django.utils import timezone

# Create your views here.


# 注册功能
@csrf_exempt  # 处理跨域
def userRegister(request):
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


# 登录功能
@csrf_exempt  # 处理跨域
def userLogin(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中文不乱码，用json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    # print(reqBody)
    username = reqBody['userName']
    password = reqBody['userPassword']
    if username and password:
        # 查找符合条件的用户信息
        user = User.objects.filter(userName=username)
        if user.exists():
            if user.first().userPassword != password:
                return JsonResponse({'code': 0, 'msg': '密码输入错误'})
            else:
                userInfo = (json.loads(serializers.serialize("json", user)))[0]

                # 当前的所有session--防止重复登录
                valid_session_obj_list = Session.objects.filter(expire_date__gt=timezone.now())
                flag = 0
                for session_obj in valid_session_obj_list:
                    print(session_obj.get_decoded().get("userInfo"))
                    if session_obj.get_decoded().get("userInfo").pk == userInfo.pk:
                        flag = 1
                        break
                if flag == 0:
                    # 将所登录的用户信息存储在session中（已经改session的默认存储位置为redis中），返回给前端的cookie是sessionid
                    # 只要前端每次请求都带上cookie，后端便可根据每个用户的sessionid查找或者操作对应的登录状态和登录信息
                    request.session['userInfo'] = userInfo
                    # 这句话完成了下面几步：
                    # 1.生成随机的sessionid字符串
                    # 2.将sessionid和用户的信息在数据库中保存为一个键值对
                    # 3.通过cookie将sessionid保存在客户端上
                    # 这时候通过用户再次向服务器发送请求时服务器就可以通过请求中的sessionid判断用户的信息了，从而达到保存登录状态的要求。

                    # 返回登录成功信息给前端
                    return JsonResponse({'code': 0, 'msg': 'success', 'userInfo': userInfo})
                else:
                    return JsonResponse({'code': -1, 'msg': '该用户已登录', 'userInfo': userInfo})
        else:
            return JsonResponse({'code': -1, "msg": "该用户不存在"})
    else:
        return JsonResponse({'code': -1, "msg": "用户名或密码不能为空"})


# 获取当前登录信息
@csrf_exempt  # 处理跨域
def getLoginUser(request):
    try:
        userInfo = request.session.get('userInfo', None)
        if userInfo:
            # 返回登录成功信息给前端
            return JsonResponse({'code': 0, 'msg': 'success', 'userInfo': userInfo})
        else:
            return JsonResponse({'code': -1, "msg": "未查找到登录信息"})
    # 防止异常处理太过宽泛
    except AttributeError:
        return JsonResponse({'code': -2, 'msg': '发生异常'})


# 退出登录
@csrf_exempt  # 处理跨域
def loginOut(request):
    try:
        # 退出登录的前提是已经登录
        userInfo = request.session.get('userInfo', None)
        if userInfo:
            # 清除该用户在服务器中的session，删除客户端的sessionid在服务器中保存的状态
            del request.session['userInfo']
            # 返回退出成功信息给前端
            return JsonResponse({'code': 0, 'msg': 'success'})
        else:
            return JsonResponse({'code': -1, 'msg': '当前用户未登录'})
    # 防止异常处理太过宽泛
    except AttributeError:
        return JsonResponse({'code': -2, 'msg': '退出失败'})
