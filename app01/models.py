from django.db import models
from django.db.models import Max, Count
# 导入`connection`用于执行原生sql语句
from django.db import connection

# Create your models here.


# 系统用户user表：【userId，userName，userPassword，userPower，createTime，updateTime】
class User(models.Model):
    # primary_key=True表示该属性为该表的主键，暗示null=False和unique=True。
    id = models.AutoField(primary_key=True)

    userId = models.CharField(max_length=20)
    userName = models.CharField(unique=True, max_length=15)
    userPassword = models.CharField(max_length=20)
    userPower = models.DecimalField(max_digits=3, decimal_places=0, default=10)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.id:
            idCount = User.objects.aggregate(Count('id')).get("id__count")
            cursor = connection.cursor()
            if idCount == 0:
                # 要想使用sql原生语句，必须用到execute()函数,然后在里面写入sql原生语句
                cursor.execute("TRUNCATE app01_user RESTART IDENTITY")
            maxid = User.objects.aggregate(Max('id')).get("id__max")
            # 让主键从什么位置开始排序
            if maxid is not None:
                cursor.execute("ALTER SEQUENCE app01_user_id_seq RESTART WITH %s", [maxid+1])
            self.userId = "{}{:06d}".format('user', (maxid+1) if maxid is not None else 1)
        super().save(*kwargs)


# 物品ware表：【wareId，wareName，warePower，wareCount，createTime，updateTime】
class Ware(models.Model):
    id = models.AutoField(primary_key=True)

    wareId = models.CharField(max_length=20)
    wareName = models.CharField(unique=True, max_length=15)
    warePower = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    wareCount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.id:
            idCount = Ware.objects.aggregate(Count('id')).get("id__count")
            cursor = connection.cursor()
            if idCount == 0:
                # 要想使用sql原生语句，必须用到execute()函数,然后在里面写入sql原生语句
                cursor.execute("TRUNCATE app01_ware RESTART IDENTITY")
            maxid = Ware.objects.aggregate(Max('id')).get("id__max")
            # 让主键从什么位置开始排序
            if maxid is not None:
                cursor.execute("ALTER SEQUENCE app01_ware_id_seq RESTART WITH %s", [maxid+1])
            self.wareId = "{}{:06d}".format('ware', (maxid+1) if maxid is not None else 1)
        super().save(*kwargs)


# 订单order表：【orderId，userId，userName，wareId，wareName，wareCount，createTime】
class Order(models.Model):
    id = models.AutoField(primary_key=True)

    orderId = models.CharField(max_length=20)
    userId = models.CharField(max_length=20)
    userName = models.CharField(max_length=15)
    wareId = models.CharField(max_length=20)
    wareName = models.CharField(max_length=15)
    wareCount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    createTime = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        if not self.id:
            idCount = Order.objects.aggregate(Count('id')).get("id__count")
            cursor = connection.cursor()
            if idCount == 0:
                # 要想使用sql原生语句，必须用到execute()函数,然后在里面写入sql原生语句
                cursor.execute("TRUNCATE app01_order RESTART IDENTITY")
            maxid = Order.objects.aggregate(Max('id')).get("id__max")
            # 让主键从什么位置开始排序
            if maxid is not None:
                cursor.execute("ALTER SEQUENCE app01_order_id_seq RESTART WITH %s", [maxid+1])
            self.orderId = "{}{:06d}".format('order', (maxid+1) if maxid is not None else 1)
        super().save(*kwargs)


# 临时订单cart表：【cartId，userId，userName，wareId，wareName，wareCount，createTime，updateTime】
class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    cartId = models.CharField(max_length=20)
    userId = models.CharField(max_length=20)
    userName = models.CharField(max_length=15)
    wareId = models.CharField(max_length=20)
    wareName = models.CharField(max_length=15)
    wareCount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.id:
            idCount = Cart.objects.aggregate(Count('id')).get("id__count")
            cursor = connection.cursor()
            if idCount == 0:
                # 要想使用sql原生语句，必须用到execute()函数,然后在里面写入sql原生语句
                cursor.execute("TRUNCATE app01_cart RESTART IDENTITY")
            maxid = Cart.objects.aggregate(Max('id')).get("id__max")
            # 让主键从什么位置开始排序
            if maxid is not None:
                cursor.execute("ALTER SEQUENCE app01_cart_id_seq RESTART WITH %s", [maxid+1])
            self.cartId = "{}{:06d}".format('cart', (maxid+1) if maxid is not None else 1)
        super().save(*kwargs)


# 公司销售额sales表：【salesId，yearName，yearSales，yearEvents，monthSales，wareSales】
class Sales(models.Model):
    id = models.AutoField(primary_key=True)

    salesId = models.CharField(max_length=20)
    yearName = models.CharField(max_length=5)
    yearSales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    yearEvents = models.CharField(max_length=30, default="")
    monthSales = models.JSONField(null=True)
    wareSales = models.JSONField(null=True)

    def save(self, **kwargs):
        if not self.id:
            idCount = Sales.objects.aggregate(Count('id')).get("id__count")
            cursor = connection.cursor()
            if idCount == 0:
                # 要想使用sql原生语句，必须用到execute()函数,然后在里面写入sql原生语句
                cursor.execute("TRUNCATE app01_sales RESTART IDENTITY")
            maxid = Sales.objects.aggregate(Max('id')).get("id__max")
            # 让主键从什么位置开始排序
            if maxid is not None:
                cursor.execute("ALTER SEQUENCE app01_sales_id_seq RESTART WITH %s", [maxid+1])
            self.salesId = "{}{:06d}".format('sales', (maxid+1) if maxid is not None else 1)
        super().save(*kwargs)

