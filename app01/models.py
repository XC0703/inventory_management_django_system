from django.db import models
from django.db.models import Max

# Create your models here.


# 系统用户user表：【userId，userName，userPassword，userPower，createTime，updateTime】
class User(models.Model):
    # primary_key=True表示该属性为该表的主键，暗示null=False和unique=True。
    userId = models.CharField(primary_key=True, max_length=20)
    userName = models.CharField(unique=True, max_length=15)
    userPassword = models.CharField(max_length=20)
    userPower = models.DecimalField(max_digits=3, decimal_places=0, default=10)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.userId:
            maxuserid = User.objects.aggregate(userId_max=Max('userId'))['userId_max']
            self.userId = "{}{:06d}".format('user', maxuserid if maxuserid is not None else 1)
        super().save(*kwargs)


# 物品ware表：【wareId，wareName，warePower，wareCount，createTime，updateTime】
class Ware(models.Model):
    wareId = models.CharField(primary_key=True, max_length=20)
    wareName = models.CharField(unique=True, max_length=15)
    warePower = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    wareCount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.wareId:
            maxwareid = Ware.objects.aggregate(wareId_max=Max('wareId'))['wareId_max']
            self.wareId = "{}{:06d}".format('ware', maxwareid if maxwareid is not None else 1)
        super().save(*kwargs)


# 订单order表：【orderId，userId，userName，wareId，wareName，wareCount，createTime】
class Order(models.Model):
    orderId = models.CharField(primary_key=True, max_length=20)
    userId = models.CharField(max_length=20)
    userName = models.CharField(unique=True, max_length=15)
    wareId = models.CharField(max_length=20)
    wareCount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    createTime = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        if not self.orderId:
            maxorderid = Order.objects.aggregate(orderId_max=Max('orderId'))['orderId_max']
            self.orderId = "{}{:06d}".format('order', maxorderid if maxorderid is not None else 1)
        super().save(*kwargs)


# 临时订单cart表：【orderId，userId，userName，wareId，wareName，wareCount，createTime】
class Cart(models.Model):
    cartId = models.CharField(primary_key=True, max_length=20)
    userId = models.CharField(max_length=20)
    userName = models.CharField(unique=True, max_length=15)
    wareId = models.CharField(max_length=20)
    wareCount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    createTime = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        if not self.cartId:
            maxcartid = Cart.objects.aggregate(cartId_max=Max('cartId'))['cartId_max']
            self.cartId = "{}{:06d}".format('cart', maxcartid if maxcartid is not None else 1)
        super().save(*kwargs)


# 公司销售额sales表：【salesId，yearName，yearSales，yearEvents，monthSales，wareSales】
class Sales(models.Model):
    salesId = models.CharField(primary_key=True, max_length=20)
    yearName = models.CharField(max_length=5)
    yearSales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    yearEvents = models.CharField(max_length=30, default="")
    monthSales = models.JSONField(null=True)
    wareSales = models.JSONField(null=True)

    def save(self, **kwargs):
        if not self.salesId:
            maxsalesid = Sales.objects.aggregate(salesId_max=Max('salesId'))['salesId_max']
            self.salesId = "{}{:06d}".format('sales', maxsalesid if maxsalesid is not None else 1)
        super().save(*kwargs)



