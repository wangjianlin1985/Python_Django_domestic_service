from django.contrib import admin
from django.urls import path, include
from MyApp import views as App_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MyApp/', include('MyApp.urls')),
#登录注册：
    path('login/', App_views.login),
    path('customer_register/', App_views.customer_register),
    path('worker_register/', App_views.worker_register),
    path('login_judge/', App_views.login_judge),

#客户界面：
    path('customer_information/', App_views.customer_information),
    path('customer_appoint/', App_views.customer_appoint),
    path('appoint_record/', App_views.appoint_record),
    path('worker_detail/', App_views.worker_detail),
    path('change_customer_password/', App_views.change_customer_password),

#员工界面：
    path('worker_information/', App_views.worker_information),
    path('order_record/', App_views.order_record),
    path('finance_infomation/', App_views.finance_infomation),
    path('change_worker_password/', App_views.change_worker_password),

    path('', App_views.login),
]

