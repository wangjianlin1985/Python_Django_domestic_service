# Generated by Django 2.2.1 on 2020-04-21 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_name', models.CharField(max_length=50, verbose_name='姓名')),
                ('customer_sex', models.CharField(max_length=10, verbose_name='性别')),
                ('customer_age', models.CharField(max_length=10, verbose_name='年龄')),
                ('customer_telephone', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='电话')),
                ('customer_address', models.CharField(max_length=50, verbose_name='住址')),
                ('customer_id', models.CharField(max_length=50, unique=True, verbose_name='身份证号')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.AutoField(max_length=50, primary_key=True, serialize=False, verbose_name='类型编号')),
                ('type_name', models.CharField(max_length=50, verbose_name='类型名称')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_telephone', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='账户')),
                ('user_password', models.CharField(max_length=50, verbose_name='密码')),
                ('user_identity', models.CharField(max_length=50, verbose_name='身份')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('worker_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='员工编号')),
                ('worker_name', models.CharField(max_length=50, verbose_name='姓名')),
                ('worker_sex', models.CharField(max_length=50, verbose_name='性别')),
                ('worker_age', models.CharField(max_length=50, verbose_name='年龄')),
                ('worker_address', models.CharField(max_length=50, verbose_name='地址')),
                ('worker_idcard', models.CharField(max_length=50, verbose_name='身份证号')),
                ('worker_experience', models.CharField(max_length=50, verbose_name='')),
                ('worker_salary', models.CharField(max_length=50, verbose_name='工资')),
                ('worker_information', models.CharField(max_length=50, verbose_name='个人简介')),
                ('worker_telephone', models.CharField(max_length=50, unique=True, verbose_name='电话')),
                ('worker_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Type', verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单编号')),
                ('order_price', models.FloatField(verbose_name='订单金额')),
                ('order_time', models.CharField(max_length=50, verbose_name='下单时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Customer', verbose_name='订单客户')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Worker', verbose_name=' 家政人员')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_cost', models.FloatField(verbose_name='平台支出')),
                ('income', models.FloatField(verbose_name='净收入')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Order', verbose_name='订单')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Worker', verbose_name='员工')),
            ],
        ),
    ]
