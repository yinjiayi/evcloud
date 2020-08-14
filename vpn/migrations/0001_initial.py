# Generated by Django 2.2.14 on 2020-07-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPNAuth',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('active', models.BooleanField(default=True, verbose_name='激活状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('create_user', models.CharField(default='', max_length=255, verbose_name='创建者')),
                ('modified_user', models.CharField(default='', max_length=255, verbose_name='修改者')),
                ('remarks', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
            ],
            options={
                'verbose_name': 'VPN',
                'verbose_name_plural': 'VPN',
                'db_table': 'vpn_auth',
                'ordering': ['-id'],
            },
        ),
    ]