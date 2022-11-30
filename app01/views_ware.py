# 导入所需模块
from app01.models import *
# 处理跨域
from django.views.decorators.csrf import csrf_exempt
# JSON对象序列化
import json
from django.http import JsonResponse


# wareId
# wareName
# warePower
# wareCount


# 库存管理
# 新增库存功能
@csrf_exempt  # 处理跨域
def addWare(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中文不乱码，用json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    # print(reqBody)
    warename = reqBody['wareName']
    count = reqBody['wareCount']
    warepower = reqBody['warePower']
    if warename and count and warepower:
        # 判断字符串长度
        if len(warename) > 15:
            return JsonResponse({'code': -1, 'msg': '物品名过长'})
        # 查找数据库中是否已经存在相同的wareName
        waren_name = Ware.objects.filter(wareName=warename)
        if waren_name.exists():
            return JsonResponse({'code': -1, 'msg': '物品名已存在'})
        # 如果不重复，在保存有关信息
        # warePower最大值为三位数
        ware_save = Ware(wareName=warename, wareCount=count, warePower=warepower)
        ware_save.save()
        # 返回注册成功信息给前端
        return JsonResponse({'code': 0, 'msg': 'success'})
    else:
        return JsonResponse({'code': -1, "msg": "物品信息不能为空"})


# 删除物品功能
@csrf_exempt  # 处理跨域
def deleteWare(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    try:
        for wareid in reqBody:
            ware_id = Ware.objects.filter(wareId=wareid)
            if not ware_id.exists():
                return JsonResponse({'code': -1, 'msg': '删除失败，数据不存在', '错误发生id': wareid})
            else:
                Ware.objects.filter(wareId=wareid).delete()
        return JsonResponse({'code': 0, 'msg': 'success'})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '物品删除失败'})


# 更改物品功能
@csrf_exempt  # 处理跨域
def changeWare(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    wareid = reqBody['wareId']
    warename = reqBody['wareName']
    Count = reqBody['wareCount']
    power = reqBody['warePower']
    if warename and Count and power:
        # 判断字符串长度
        if len(warename) > 15:
            return JsonResponse({'code': -1, 'msg': '物品名过长'})
        # 查找数据库中是否已经存在相同的wareId
        Ware_id = Ware.objects.filter(wareId=wareid)
        if not Ware_id.exists():
            return JsonResponse({'code': -1, 'msg': '修改失败，id不存在'})
        ware_name = Ware.objects.filter(wareName=warename)
        if ware_name.exists():
            warename_ori = Ware.objects.get(wareId=wareid).wareName
            if not warename == warename_ori:
                return JsonResponse({'code': -1, 'msg': '物品名已存在'})
        # 如果id存在，保存有关信息
        Ware.objects.filter(wareId=wareid).update(wareName=warename, wareCount=Count, warePower=power)
        # 返回成功信息给前端
        return JsonResponse({'code': 0, 'msg': 'success'})
    else:
        return JsonResponse({'code': -1, "msg": "物品信息不能为空"})

    # 查询全部货物


@csrf_exempt  # 处理跨域
def getWarelist(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    # reqBody = json.loads(request.body.decode())
    qs = Ware.objects.values()
    try:
        # 将QuerySet对象转化为list类型
        # 否则不能被转化为JSON字符串
        retlist = list(qs)
        return JsonResponse({'code': 0, 'msg': 'success', 'wareInfo': retlist})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取物品信息失败'})

    # 查询单个物品


@csrf_exempt  # 处理跨域
def getWare(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中⽂不乱
    # 码，⽤json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    ware_id_info = Ware.objects.filter(wareId=reqBody).values()
    ware_id = Ware.objects.filter(wareId=reqBody)
    if not ware_id.exists():
        return JsonResponse({'code': -1, 'msg': '该物品信息不存在'})
    try:
        ware_info = list(ware_id_info)[0]
        return JsonResponse({'code': 0, 'msg': 'success', 'wareInfo': ware_info})
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取物品信息失败'})
