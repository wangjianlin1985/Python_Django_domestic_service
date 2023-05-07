import datetime
from django.db.models import Q
from django.forms import model_to_dict
from django.shortcuts import render
from MyApp.models import *
user_telephone=""
global_cname=""
global_wname=""

def login(request):#登录
    return render(request, 'login.html')

def customer_register(request):  # 客户注册
    if request.method == "GET":
        return render(request, 'customer_register.html')
    else:
        customer_name = request.POST.get("customer_name")  # 获取客户输入的姓名
        customer_sex = request.POST.get("customer_sex")  # 获取客户输入的性别
        customer_age = request.POST.get("customer_age")  # 获取客户输入的年龄
        customer_telephone = request.POST.get("customer_telephone")  # 获取客户输入的电话
        customer_address = request.POST.get("customer_address")
        customer_id = request.POST.get("customer_id")
        customer_password = request.POST.get("customer_password")
        result1 = User.objects.filter(user_telephone=customer_telephone)  # 在用户表中搜索该用户名的记录
        result2 = Customer.objects.filter(customer_id=customer_id)  # 在客户表中搜索该身份证号的使用记录
        context = {}
        if len(result1) == 1:  # 判断该账户是否存在(即判断是否注册过)，如果后台存在记录，则返回相应的提示语句
            context["info"] = "该账户已注册！！！"
            context["status"] = 0  #零表示注册失败
            return render(request, 'customer_register.html', context=context)
        else:  #该账户是新用户
            if len(result2) == 1:#判断该身份证号是否有客户已注册
                context["info"] = "该身份证号已占用！！！"
                context["status"] = 4
                return render(request, 'customer_register.html', context=context)
            else:
                User.objects.create(user_telephone=customer_telephone, user_password=customer_password,user_identity='客户')#用create为user表添加一条记录
                Customer.objects.create(customer_name=customer_name,customer_id=customer_id,customer_address=customer_address,customer_sex=customer_sex,customer_age=customer_age,customer_telephone=customer_telephone)#用create为Patient表添加一条记录
                return render(request, 'login.html')

def worker_register(request):  # 员工注册
    if request.method == "GET":
        types = Type.objects.all()
        return render(request, 'worker_register.html',context={"types":types})
    else:
        types = Type.objects.all()
        worker_name = request.POST.get("worker_name")  # 获取员工输入的姓名
        worker_id = request.POST.get("worker_id") # 获取员工输入的工号
        worker_sex = request.POST.get("worker_sex")
        worker_age = request.POST.get("worker_age")
        worker_telephone = request.POST.get("worker_telephone")
        worker_type = request.POST.get("worker_type")
        worker_idcard = request.POST.get("worker_idcard")
        worker_password = request.POST.get("worker_password")
        type = Type.objects.filter(type_id=int(worker_type)).first()
        result1 = User.objects.filter(user_telephone=worker_telephone)  # 在用户表中搜索该用户名的记录
        result2 = Worker.objects.filter(worker_id=worker_id)  # 在员工表中搜索该工号的使用记录
        context = {}
        if len(result1) == 1:  # 判断该账户是否存在(即判断是否注册过)，如果后台存在记录，则返回相应的提示语句
            context["info"] = "该账户已注册！！！"
            context["status"] = 0  #零表示注册失败
            context["types"] = types
            return render(request, 'worker_register.html',context=context)
        else:  #该账户是新用户
            if len(result2) == 1:#判断该工号号是否有员工已使用
                context["info"] = "该工号已占用！！！"
                context["status"] = 5
                context["types"] = types
                return render(request, 'worker_register.html', context=context)
            else:
                User.objects.create(user_telephone=worker_telephone, user_password=worker_password,user_identity='员工')#用create为user表添加一条记录
                Worker.objects.create(worker_name=worker_name,worker_telephone=worker_telephone,worker_type=type, worker_id=worker_id, worker_sex=worker_sex, worker_age=worker_age,
                                      worker_idcard=worker_idcard)#用create为Doctor表添加一条记录
                return render(request, 'login.html')

def login_judge(request):#登入判定
    global user_telephone ,global_cname,global_wname #定义全局变量user_telephone,存储当前登入用户的账户，global_cname保存一下该客户的姓名,global_wname保存一下该员工的姓名
    user_telephone = request.POST.get("telephone")#获取前端输入的账户
    user_password = request.POST.get("password")
    print(user_telephone)
    result1 = User.objects.filter(user_telephone=user_telephone)#在user表里检索是否存在该账户
    if len(result1) == 1:  # 判断后台是否存在该用户，有则进一步判断密码是否正确
        password = result1[0].user_password  # 获取后台的密码
        identity = result1[0].user_identity  # 获取该账户的身份信息
        if user_password == password:  # 将用户输入的密码和后台密码进行比对,如何正确，判断该账户身份
            if identity == '客户':
                result2 = Customer.objects.filter(customer_telephone=user_telephone)
                global_cname = result2[0].customer_name  # 用全局变量保存一下该客户的姓名
                context = {
                    "customer_id": result2[0].customer_id,
                    "customer_name": result2[0].customer_name,
                    "customer_sex": result2[0].customer_sex,
                    "customer_age": result2[0].customer_age,
                    "customer_telephone": result2[0].customer_telephone,
                    "customer_address": result2[0].customer_address,
                    "name":global_cname
                }
                return render(request, 'customer/customer_information.html', context)  # 跳转到客户主页界面
            elif identity == '员工':
                result = Worker.objects.filter(worker_telephone=user_telephone)  # user_telephone为全局变量
                global_wname = result[0].worker_name  # 用全局变量保存一下该员工的姓名
                types = Type.objects.all()
                context = {
                    "worker_id": result[0].worker_id,
                    "worker_name": result[0].worker_name,
                    "worker_sex": result[0].worker_sex,
                    "worker_age": result[0].worker_age,
                    "worker_address": result[0].worker_address,
                    "worker_idcard": result[0].worker_idcard,
                    "worker_experience": result[0].worker_experience,
                    "worker_salary": result[0].worker_salary,
                    "worker_information": result[0].worker_information,
                    "worker_type": result[0].worker_type.type_name,
                    "worker_telephone": result[0].worker_telephone,
                    "name":global_wname,
                    "types":types
                }
                return render(request, 'worker/worker_information.html', context)  # 跳转到客户主页界面
            elif identity == '管理员':#若为管理员，则直接跳转到管理员界面
                workers = Worker.objects.all()
                return render(request, 'manager/docotr_manage.html', context={"workers": workers})# 跳转到管理员界面
            else:
                return render(request, 'login.html')  # 密码错误回到登入界面
        else:  # 如果不一致则返回相应提示语句
            context = {
                "info": "密码错误！！！",
                "status": 2
            }
            return render(request, 'login.html', context=context)  # 密码错误回到登入界面
    else:  # 如果不存在该用户则返回相应的提示语句
        context = {
            "info": "该账户不存在！！！",
            "status": 3
        }
        return render(request, 'login.html', context=context)  # 账户不存在则继续回到登入界面

#客户界面
def customer_information(request):#个人信息
    if request.method == "GET":  #此部分是当每次点击横向导航栏的“个人信息”选项时，都重新显示该用户的个人资料
        result = Customer.objects.filter(customer_telephone=user_telephone)  #user_telephone为全局变量
        context = {
            "customer_id": result[0].customer_id,
            "customer_name": result[0].customer_name,
            "customer_sex": result[0].customer_sex,
            "customer_age": result[0].customer_age,
            "customer_telephone": result[0].customer_telephone,
            "customer_address": result[0].customer_address,
            "name": global_cname
        }
        return render(request, 'customer/customer_information.html', context)#将该用户的个人信息再次传到前端页面
    else:  #在customer_information.html页面中通过post方式的“保存”按钮跳转到此处，即完成更新数据操作（保存）
        customer_age = request.POST.get("customer_age")  # 获取年龄
        customer_address = request.POST.get("customer_address")  # 获取地址
        Customer.objects.filter(customer_telephone=user_telephone).update(customer_age=customer_age,customer_address=customer_address)#更新数据
        result = Customer.objects.filter(customer_telephone=user_telephone)  # user_telephone为全局变量   此处再次传值到前端
        context = {
            "customer_id": result[0].customer_id,
            "customer_name": result[0].customer_name,
            "customer_sex": result[0].customer_sex,
            "customer_age": result[0].customer_age,
            "customer_telephone": result[0].customer_telephone,
            "customer_address": result[0].customer_address,
            "name": global_cname
        }
        return render(request, 'customer/customer_information.html', context)  # 将该用户的个人信息再次传到前端页面

def customer_appoint(request):#家政选聘
    if request.method == "GET":#此部分是当用户每次点击侧边导航栏的“家政市场”选项时，都要显示出所有家政人员信息
        workers = Worker.objects.all()
        types = Type.objects.all()
        return render(request, 'customer/customer_appoint.html',context={"workers": workers,"types":types,"name":global_cname })
    else:#customer/customer_appoint.html页面中通过post方式的“搜索”按钮跳转到此处，即完成搜索操作
        type_id = request.POST.get("type_id")
        types = Type.objects.all()
        workers = Worker.objects.all()
        if type_id and type_id!="0":
            rusults = Worker.objects.filter(worker_type=int(type_id))
            if rusults:#如果找到的结果集非空，则输出
                return render(request,'customer/customer_appoint.html',context={"workers":rusults,"types":types,"name":global_wname})
            else:#若搜索的结果集为0，那么输出未找到该类型的家政人员！
                return render(request,'customer/customer_appoint.html',context={"workers":workers,"types":types,"name":global_wname,"status":0})
        else:
            return render(request, 'customer/customer_appoint.html',
                          context={"workers": workers, "types": types, "name": global_wname})

def worker_detail(request):#点击详情时调用此函数
    global worker_id
    if request.method == "GET":
        worker_id = request.GET.get("worker_id")
        result = Worker.objects.filter(worker_id = worker_id)
        context = {
            "worker_name": result[0].worker_name,
            "worker_sex": result[0].worker_sex,
            "worker_age": result[0].worker_age,
            "worker_address": result[0].worker_address,
            "worker_idcard": result[0].worker_idcard,
            "worker_experience": result[0].worker_experience,
            "worker_salary": result[0].worker_salary,
            "worker_information": result[0].worker_information,
            "worker_type": result[0].worker_type,
            "worker_telephone": result[0].worker_telephone,
            "name": global_cname

        }
        return render(request, 'customer/worker_detail.html',context)  # 向前端传递所有预约记录的集合
    else:
        workers = Worker.objects.all()
        types = Type.objects.all()
        worker=Worker.objects.filter(worker_id=worker_id).first()
        customer=Customer.objects.filter(customer_telephone =user_telephone ).first()
        order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        price = worker.worker_salary
        Order.objects.create(worker=worker,customer=customer,order_price=worker.worker_salary,order_time=order_time)
        order = Order.objects.filter(order_time=order_time).first()
        platform_cost = float(price) * 0.1
        income = float(price)-platform_cost
        Finance.objects.create(order = order,platform_cost=platform_cost,income=income,worker=worker)
        return render(request, 'customer/customer_appoint.html',
                      context={"workers": workers, "types": types, "name": global_cname})


def appoint_record(request):#订单记录
    if request.method == "GET":#此部分是当用户每次点击横向导航栏的“订单记录”选项时
        customer = Customer.objects.filter(customer_telephone=user_telephone).first()
        records = Order.objects.filter(customer=customer)
        return render(request, 'customer/appoint_record.html',context={"records":records,"name":global_cname })  # 向前端传递所有订单记录的集合


def change_customer_password(request):#修改密码
    result = User.objects.filter(user_telephone=user_telephone).first()
    password = result.user_password
    if request.method == "GET": #此部分是当每次点击横向导航栏的“修改密码”选项时，显示该界面
        return render(request,'customer/change_customer_password.html',context={"password":password,"name":global_cname})
    else:#此部分是在change_customer_password.html页面中点击保存按钮时完成修改密码的操作
        oldPassword = request.POST.get("oldPassword")
        newPassword = request.POST.get("newPassword")
        reNewPassword = request.POST.get("reNewPassword")#以下是先判断输入的旧密码是否正确，并且两次输入的密码是否一致且都不为空
        if password == oldPassword and newPassword == reNewPassword and newPassword and reNewPassword:
            User.objects.filter(user_telephone=user_telephone).update(user_password = newPassword)#更新该用户的密码
            password = newPassword
        return render(request, 'customer/change_customer_password.html', context={"password": password, "name": global_cname})

#员工界面
def worker_information(request):#个人信息
    if request.method == "GET":  #此部分是当每次点击横向导航栏的“个人信息”选项时，都重新显示该用户的个人资料
        result = Worker.objects.filter(worker_telephone=user_telephone)  #user_telephone为全局变量
        types = Type.objects.all()
        context = {
            "worker_id": result[0].worker_id,
            "worker_name": result[0].worker_name,
            "worker_sex": result[0].worker_sex,
            "worker_age": result[0].worker_age,
            "worker_address": result[0].worker_address,
            "worker_idcard": result[0].worker_idcard,
            "worker_experience": result[0].worker_experience,
            "worker_salary": result[0].worker_salary,
            "worker_information": result[0].worker_information,
            "worker_type": result[0].worker_type.type_name,
            "worker_telephone": result[0].worker_telephone,
            "name": global_wname,
            "types": types
        }
        return render(request, 'worker/worker_information.html', context)#将该用户的个人信息再次传到前端页面

    else:  #在worker_information.html页面中通过post方式的“保存”按钮跳转到此处，即完成更新数据操作（保存）
        worker_name = request.POST.get("worker_name")  # 获取年龄
        worker_sex = request.POST.get("worker_sex")
        worker_age = request.POST.get("worker_age")
        worker_address = request.POST.get("worker_address")
        worker_idcard = request.POST.get("worker_idcard")
        worker_experience = request.POST.get("worker_experience")
        worker_salary = request.POST.get("worker_salary")
        worker_information = request.POST.get("worker_information")
        worker_type = request.POST.get("worker_type")
        type = Type.objects.filter(type_name = worker_type).first()
        flag=0
        result = Worker.objects.filter(worker_telephone=user_telephone)  # user_telephone为全局变量   此处再次传值到前端
        if worker_salary.isdigit():
            flag = 1
            Worker.objects.filter(worker_telephone=user_telephone).update(worker_name=worker_name,worker_sex=worker_sex,worker_age=worker_age,
            worker_address=worker_address,worker_idcard=worker_idcard,worker_experience=worker_experience,worker_salary=int(worker_salary),worker_information=worker_information,worker_type=type)#更新数据
        types = Type.objects.all()
        context = {
            "worker_id": result[0].worker_id,
            "worker_name": result[0].worker_name,
            "worker_sex": result[0].worker_sex,
            "worker_age": result[0].worker_age,
            "worker_address": result[0].worker_address,
            "worker_idcard": result[0].worker_idcard,
            "worker_experience": result[0].worker_experience,
            "worker_salary": result[0].worker_salary,
            "worker_information": result[0].worker_information,
            "worker_type": result[0].worker_type.type_name,
            "worker_telephone": result[0].worker_telephone,
            "name": global_wname,
            "types": types,
            "status": flag
        }
        return render(request, 'worker/worker_information.html', context)  # 跳转到客户主页界面


def order_record(request):#员工界面的订单记录
    if request.method == "GET":  # 此部分是当用户每次点击横向导航栏的“订单记录”选项时
        worker = Worker.objects.filter(worker_telephone=user_telephone).first()
        records = Order.objects.filter(worker=worker)
        return render(request, 'worker/order_record.html',
                      context={"records": records, "name": global_wname})  # 向前端传递所有订单记录的集合


def finance_infomation(request):#财务信息页面
    worker = Worker.objects.filter(worker_telephone=user_telephone).first()
    records = Finance.objects.filter(worker=worker)
    rest=0.0
    for i in records:
        rest = rest + i.income
    print(rest)
    return render(request, 'worker/finance_infomation.html',
                  context={"records": records, "name": global_wname,"rest_money":rest})  # 向前端传递所有财务信息的集合


def change_worker_password(request):#修改密码
    result = User.objects.filter(user_telephone=user_telephone).first()
    password = result.user_password
    if request.method == "GET": #此部分是当每次点击横向导航栏的“修改密码”选项时，显示该界面
        return render(request,'worker/change_worker_password.html',context={"password":password,"name":global_wname})
    else:#此部分是在change_worker_password.html页面中点击保存按钮时完成修改密码的操作
        oldPassword = request.POST.get("oldPassword")
        newPassword = request.POST.get("newPassword")
        reNewPassword = request.POST.get("reNewPassword")#以下是先判断输入的旧密码是否正确，并且两次输入的密码是否一致且都不为空
        if password == oldPassword and newPassword == reNewPassword and newPassword and reNewPassword:
            User.objects.filter(user_telephone=user_telephone).update(user_password = newPassword)#更新该用户的密码
            password = newPassword
        return render(request, 'worker/change_worker_password.html', context={"password": password, "name": global_wname})


