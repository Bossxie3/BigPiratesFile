# Generated by Django 3.0.6 on 2022-02-23 01:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_number_name', models.CharField(max_length=20, verbose_name='大编号名')),
                ('big_number_num', models.IntegerField(default=0, verbose_name='大编号序号')),
                ('small_number', models.IntegerField(default=0, verbose_name='小编号序号')),
            ],
        ),
        migrations.CreateModel(
            name='CacheFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255, verbose_name='文件名')),
                ('file_adr', models.CharField(max_length=255, verbose_name='文件地址')),
                ('big_number_name', models.CharField(max_length=20, verbose_name='大编号名')),
                ('big_number_num', models.IntegerField(default=0, verbose_name='大编号序号')),
                ('small_number', models.IntegerField(default=0, verbose_name='小编号序号')),
                ('production_date', models.DateField(verbose_name='制作日期')),
                ('producer', models.CharField(max_length=20, verbose_name='制作人')),
                ('game_name', models.CharField(choices=[(0, 'NSG'), (1, 'AOW')], max_length=20, verbose_name='游戏名')),
                ('content', models.CharField(max_length=255, verbose_name='视频内容')),
                ('size', models.CharField(choices=[(0, '16:9'), (1, '9:16'), (2, '1:1')], max_length=20, verbose_name='尺寸')),
                ('make_mode', models.CharField(choices=[(0, 'UE'), (1, 'AE'), (2, '剪辑')], max_length=20, verbose_name='制作模式')),
                ('language', models.CharField(choices=[(0, 'CN'), (1, 'IN'), (2, 'VN'), (3, 'KR'), (4, 'JP'), (5, 'EN'), (6, 'ZH'), (7, 'TH'), (8, 'MY')], max_length=20, verbose_name='语言')),
                ('localization', models.CharField(choices=[(0, '原版'), (1, '改版'), (2, '预约'), (3, '立即下载')], max_length=20, verbose_name='本地化')),
                ('run_state', models.CharField(max_length=20, verbose_name='数据情况')),
                ('consumption', models.FloatField(default=0, verbose_name='消耗量')),
                ('file_type', models.CharField(choices=[(0, 'mp4'), (1, 'png'), (2, 'jpg'), (3, 'psd')], max_length=255, verbose_name='文件类型')),
                ('check_people', models.CharField(default='A', max_length=20, verbose_name='检查人')),
                ('remark', models.CharField(default='NONE', max_length=255, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255, verbose_name='文件名')),
                ('file_adr', models.CharField(max_length=255, verbose_name='文件地址')),
                ('big_number_name', models.CharField(max_length=20, verbose_name='大编号名')),
                ('big_number_num', models.IntegerField(default=0, verbose_name='大编号序号')),
                ('small_number', models.IntegerField(default=0, verbose_name='小编号序号')),
                ('production_date', models.DateField(default=datetime.datetime.now, verbose_name='制作日期')),
                ('producer', models.CharField(max_length=20, verbose_name='制作人')),
                ('game_name', models.CharField(choices=[(0, 'NSG'), (1, 'AOW')], max_length=20, verbose_name='游戏名')),
                ('content', models.CharField(max_length=255, verbose_name='视频内容')),
                ('size', models.CharField(choices=[(0, '16:9'), (1, '9:16'), (2, '1:1')], max_length=20, verbose_name='尺寸')),
                ('make_mode', models.CharField(choices=[(0, 'UE'), (1, 'AE'), (2, '剪辑')], max_length=20, verbose_name='制作模式')),
                ('language', models.CharField(choices=[(0, 'CN'), (1, 'IN'), (2, 'VN'), (3, 'KR'), (4, 'JP'), (5, 'EN'), (6, 'ZH'), (7, 'TH'), (8, 'MY')], max_length=20, verbose_name='语言')),
                ('localization', models.CharField(choices=[(0, '原版'), (1, '改版'), (2, '预约'), (3, '立即下载')], max_length=20, verbose_name='本地化')),
                ('run_state', models.CharField(max_length=20, verbose_name='数据情况')),
                ('consumption', models.FloatField(default=0, verbose_name='消耗量')),
                ('file_type', models.CharField(choices=[(0, 'mp4'), (1, 'png'), (2, 'jpg'), (3, 'psd')], max_length=255, verbose_name='文件类型')),
                ('check_people', models.CharField(default='A', max_length=20, verbose_name='检查人')),
                ('remark', models.CharField(default='NONE', max_length=255, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(choices=[(0, 'mp4'), (1, 'png'), (2, 'jpg'), (3, 'psd')], max_length=255, verbose_name='文件类型')),
                ('save_adr', models.CharField(max_length=255, verbose_name='文件对应保存地址')),
            ],
        ),
        migrations.CreateModel(
            name='PicNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_name', models.CharField(max_length=20, verbose_name='编号类型名')),
                ('number_num', models.IntegerField(default=0, verbose_name='编号序号')),
            ],
        ),
    ]
