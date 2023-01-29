# 导入所需模块
from app.models import *
# 处理跨域
from django.views.decorators.csrf import csrf_exempt
# JSON对象序列化
import json
from django.http import JsonResponse


# Create your views here.
# 新增用户功能
@csrf_exempt  # 处理跨域
def addUser(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中文不乱码，用json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    # print(reqBody)
    username = reqBody['userName']
    password = reqBody['userPassword']
    userPower = reqBody['userPower']
    if username and password and userPower:
        # 判断字符串长度
        if len(username) > 15 or len(password) > 20:
            return JsonResponse({'code': -1, 'msg': '用户名或密码过长'})
        # 查找数据库中是否已经存在相同的userName
        user_name = User.objects.filter(userName=username)
        if user_name.exists():
            return JsonResponse({'code': -1, 'msg': '用户已存在'})
        # 如果不重复，在保存有关信息
        uesr_save = User(userName=username, userPassword=password,userPower=userPower)
        uesr_save.save()
        # 返回注册成功信息给前端
        return JsonResponse({'code': 0, 'msg': 'success'})
    else:
        return JsonResponse({'code': -1, "msg": "请输入有效信息"})


# 删除用户功能
@csrf_exempt  # 处理跨域
def deleteUser(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    print(reqBody)
    try:
        for userid in reqBody:
            print(userid)
            user_id = User.objects.filter(userId=userid)
            if not user_id.exists():
                return JsonResponse({'code': -1, 'msg': '删除失败，数据不存在', '错误发生id': userid})
            else:
                User.objects.filter(userId=userid).delete()
        return JsonResponse({'code': 0, 'msg': 'success'})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '用户删除失败'})


# 更改用户功能
@csrf_exempt  # 处理跨域
def updateUser(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    userid = reqBody['userId']
    username = reqBody['userName']
    password = reqBody['userPassword']
    power = reqBody['userPower']
    if username and password and power:
        # 判断字符串长度
        if len(username) > 15 or len(password) > 20:
            return JsonResponse({'code': -1, 'msg': '用户名或密码过长'})
        # 查找数据库中是否已经存在相同的userId
        user_id = User.objects.filter(userId=userid)
        if not user_id.exists():
            return JsonResponse({'code': -1, 'msg': '修改失败，id不存在'})
        user_name = User.objects.filter(userName=username)
        if user_name.exists():
            username_ori = User.objects.get(userId=userid).userName
            if not username == username_ori:
                return JsonResponse({'code': -1, 'msg': '用户名已存在'})
        # 如果id存在，保存有关信息
        # 为什么用save不用update？因为只有在调用 Model.save() 时，该字段才会自动更新。
        # 当以其他方式对其他字段进行更新时，如 QuerySet.update()，该字段不会被更新，
        # 参考博客：http://t.csdn.cn/5uhRJ
        ret = User.objects.filter(userId=userid).first()
        ret.userName = username
        ret.userPassword = password
        ret.userPower = power
        ret.save()
        # 返回成功信息给前端
        return JsonResponse({'code': 0, 'msg': 'success'})
    else:
        return JsonResponse({'code': -1, "msg": "请输入有效信息"})


# 获取用户信息清单
@csrf_exempt  # 处理跨域
def getUserlist(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    # reqBody = json.loads(request.body.decode())
    qs = User.objects.values()
    try:
        # 将QuerySet对象转化为list类型
        # 否则不能被转化为JSON字符串
        retlist = list(qs)
        return JsonResponse({'code': 0, 'msg': 'success', 'userList': retlist})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取用户信息失败'})

    # 查询单个用户


# 获取单个用户信息
@csrf_exempt  # 处理跨域
def getUser(request, theme):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    userid = theme
    user_id_info = User.objects.filter(userId=userid).values()
    user_id = User.objects.filter(userId=userid)
    if not user_id.exists():
        return JsonResponse({'code': -1, 'msg': '该用户信息不存在'})
    try:
        user_info = list(user_id_info)[0]
        return JsonResponse({'code': 0, 'msg': 'success', 'userInfo': user_info})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取用户信息失败'})



