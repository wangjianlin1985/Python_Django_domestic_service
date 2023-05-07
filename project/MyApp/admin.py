from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from MyApp.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_telephone', 'user_password', 'user_identity')
    search_fields = ['user_identity']

admin.site.register(User, UserAdmin)

#实现用户表的导入和导出
class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        export_order = ('customer_id','customer_name', 'customer_sex','customer_age','customer_telephone','customer_address')

class CustomerAdmin(ImportExportModelAdmin):

    list_display = ('customer_name', 'customer_sex','customer_age','customer_telephone','customer_address','customer_id')
    search_fields = ['customer_name']
    list_filter = ('customer_sex','customer_address')

admin.site.register(Customer,CustomerAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'type_name')


admin.site.register(Type,TypeAdmin)

#实现员工表的导入和导出
class WorkerResource(resources.ModelResource):
    class Meta:
        model = Worker
        export_order = ('worker_id', 'worker_name','worker_sex','worker_age','worker_address','worker_idcard','worker_experience',
                    'worker_salary','worker_telephone','worker_type')

class WorkerAdmin(ImportExportModelAdmin):
    list_display = ('worker_id', 'worker_name','worker_sex','worker_age','worker_address','worker_idcard','worker_experience',
                    'worker_salary','worker_telephone','worker_type')
    search_fields = ['worker_name']
    list_filter = ('worker_sex','worker_salary','worker_experience','worker_type')
    ordering = ['worker_id'] #默认按照员工编号排序

admin.site.register(Worker,WorkerAdmin)


#实现订单表的导入和导出
class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        export_order = ('order_id', 'customer', 'worker','order_price','order_time')

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('order_id', 'customer', 'worker','order_price','order_time')
    search_fields = ['customer']

    def customer(self,obj):
        return obj.customer.customer_name

admin.site.register(Order, OrderAdmin)

#实现财务表的导出和导入
class FinanceResource(resources.ModelResource):
    class Meta:
        model = Order
        export_order = ('id','order', 'worker', 'platform_cost','income')

class FinanceAdmin(ImportExportModelAdmin):
    list_display = ['id','order', 'worker', 'platform_cost','income']
    search_fields = ['worker']

admin.site.register(Finance, FinanceAdmin)

#修改网页title和站点header。
admin.site.site_title = "家政后台管理系统"
admin.site.site_header = "家政后台管理系统"