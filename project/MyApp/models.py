from django.db import models

class User(models.Model):#用户表
    user_telephone = models.CharField(max_length=50, primary_key=True,verbose_name='账户')
    user_password = models.CharField(max_length=50,verbose_name='密码')
    user_identity = models.CharField(max_length=50,verbose_name='身份')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_telephone

class Type(models.Model):#类型表
    type_id = models.AutoField(max_length=50,primary_key=True,verbose_name='类型编号')
    type_name = models.CharField(max_length=50,verbose_name='类型名称')

    class Meta:
        verbose_name = '类型表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name

class Customer(models.Model):  #客户信息表
    customer_name = models.CharField(max_length=50,verbose_name='姓名')
    customer_sex = models.CharField(max_length=10,verbose_name='性别')
    customer_age = models.CharField(max_length=10,verbose_name='年龄')
    customer_telephone = models.CharField(max_length=50,primary_key=True,verbose_name='电话')
    customer_address = models.CharField(max_length=50,verbose_name='住址')
    customer_id = models.CharField(max_length=50,unique=True,verbose_name='身份证号')

    class Meta:
        verbose_name = '客户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.customer_name

class Worker(models.Model):  #家政人员信息表
    worker_id = models.CharField(max_length=50, primary_key=True,verbose_name='员工编号')
    worker_name = models.CharField(max_length=50,verbose_name='姓名')
    worker_sex = models.CharField(max_length=50,verbose_name='性别')
    worker_age = models.CharField(max_length=50,verbose_name='年龄')
    worker_address = models.CharField(max_length=50,verbose_name='地址')
    worker_idcard = models.CharField(max_length=50,verbose_name='身份证号')
    worker_experience = models.CharField(max_length=50,verbose_name='工作经验')
    worker_salary = models.CharField(max_length=50,verbose_name='工资')
    worker_information = models.CharField(max_length=50,verbose_name='个人简介')
    worker_telephone = models.CharField(max_length=50,unique=True,verbose_name='电话')
    worker_type = models.ForeignKey(Type, on_delete=models.CASCADE,verbose_name='类型')

    class Meta:
        verbose_name = '家政人员信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.worker_name

class Order(models.Model):  # 订单信息表
    order_id = models.AutoField(primary_key=True,verbose_name='订单编号')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name='订单客户')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,verbose_name=' 家政人员')
    order_price = models.FloatField(verbose_name='订单金额')
    order_time = models.CharField(max_length=50,verbose_name='下单时间')

    class Meta:
        verbose_name = '订单信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_time

class Finance(models.Model): #财务表
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='订单创建时间')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,verbose_name='员工')
    platform_cost = models.FloatField(verbose_name='平台收入')
    income = models.FloatField(verbose_name='员工净收入')

    class Meta:
        verbose_name = '财务表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)





