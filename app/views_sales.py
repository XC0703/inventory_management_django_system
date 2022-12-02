# 导入所需模块
from app.models import *
# 处理跨域
from django.views.decorators.csrf import csrf_exempt
# JSON对象序列化
import json
from django.core import serializers
from django.http import JsonResponse



# 将销售数据传入数据库
@csrf_exempt  # 处理跨域
def saveSalesData(request):
    # 获取前端传过来的值--request.body表示前端传过来的值，.decode()表示使中文不乱码，用json.loads转换为json格式
    reqBody = json.loads(request.body.decode())
    # print(reqBody)
    try:
        # 查找数据库中是否已经存在相同的yearName
        year_name = Sales.objects.filter(yearName=reqBody['yearName'])
        if year_name.exists():
            return JsonResponse({'code': -1, 'msg': '该年数据已存在'})
        # 如果不重复，在保存有关信息
        sales_save = Sales(yearName=reqBody['yearName'],
                           yearSales=reqBody['yearSales'],
                           yearEvents=reqBody['yearEvents'],
                           monthSales=reqBody['monthSales'],
                           wareSales=reqBody['wareSales']
                           )
        sales_save.save()
        return JsonResponse({'code': 0, 'msg': 'success'})
    # 防止异常处理太过宽泛
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '保存失败'})


# 获取数据库中的销售数据
@csrf_exempt  # 处理跨域
def getSalesData(request):
    try:
        salesData = (json.loads(serializers.serialize("json", Sales.objects.all())))
        return JsonResponse({'code': 0, 'msg': 'success', 'salesData': salesData})
    # 防止异常处理太过宽泛
    except AttributeError:
        return JsonResponse({'code': -1, 'msg': '获取失败'})