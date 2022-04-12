# models.py
from django.db import models
from datetime import datetime
import time
import django.utils.timezone as timezone

# create_time = models.DateTimeField(auto_now_add=True)
# production_date = models.DateTimeField(auto_now=True)

UseTypes = [
    (0, '广告'),
    (1, '社区'),
    (2, 'icon'),
    (3, '商店'),
    (4, '落地页'),
    (5, '官网')
]

GameTypes = [
    (0, "NSG"),
    (1, "AOW")
]

MakeTypes = [
    (0, "UE"),
    (1, "AE"),
    (2, "剪辑")
]

LocalTypes = [
    (0, "原版"),
    (1, "改版"),
    (2, "预约"),
    (3, "立即下载")
]

LanguageTypes = [
    (0, "CN"),
    (1, "IN"),
    (2, "VN"),
    (3, "KR"),
    (4, "JP"),
    (5, "EN"),
    (6, "ZH"),
    (7, "TH"),
    (8, "MY")
]

SizeTypes = [
    (0, "16:9"),
    (1, "9:16"),
    (2, "1:1")
]

FileTypes = [
    (0, 'mp4'),
    (1, 'png'),
    (2, 'jpg'),
    (3, 'psd')
]


# 总文件表
class File(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="视频内容")  # 视频内容主题
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    make_mode = models.CharField(max_length=255, choices=MakeTypes, verbose_name="制作模式")  # 制作模式，AE/UE
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3


# 图片编号表
class PicNumber(models.Model):
    number_name = models.CharField(max_length=20, verbose_name="编号类型名")  # 编号类型,CNJPG,ENJPG,CNPSD,ENPSD...
    number_num = models.IntegerField(default=0, verbose_name="编号序号")  # 编号序号，当前所用最大序号


# 视频大编号表
class BigNumber(models.Model):
    big_number_name = models.CharField(max_length=20, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号


# 缓存文件表
class CacheFile(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="视频内容")  # 视频内容主题
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    make_mode = models.CharField(max_length=255, choices=MakeTypes, verbose_name="制作模式")  # 制作模式，AE/UE
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3


# 补交视频文件表
class SuppleFile(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="视频内容")  # 视频内容主题
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    make_mode = models.CharField(max_length=255, choices=MakeTypes, verbose_name="制作模式")  # 制作模式，AE/UE
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3


# 图片文件表
class PicFile(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="系列名")  # 图片系列名
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    use = models.CharField(max_length=255, choices=UseTypes, verbose_name='用途')  # 用途，广告/商店/icon
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3


# 缓存图片文件表
class CachePicFile(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="系列名")  # 图片系列名
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    use = models.CharField(max_length=255, choices=UseTypes, verbose_name='用途')  # 用途，广告/商店/icon
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3


# 补交图片文件表
class SupplePicFile(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="系列名")  # 图片系列名
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    use = models.CharField(max_length=255, choices=UseTypes, verbose_name='用途')  # 用途，广告/商店/icon
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3


# 文件类型表
class FileType(models.Model):
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型
    save_adr = models.CharField(max_length=255, verbose_name="文件对应保存地址")  # 文件对应保存地址


# 用户名表
class User(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')


# 被删除视频文件表
class DeleteFile(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="视频内容")  # 视频内容主题
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    make_mode = models.CharField(max_length=255, choices=MakeTypes, verbose_name="制作模式")  # 制作模式，AE/UE
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    delete_time = models.DateTimeField(verbose_name='删除时间')  # 删除时间
    delete_from = models.CharField(max_length=255, verbose_name='删除来源')  # 删除来源
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3


# 被删除图片文件表
class DeletePicFile(models.Model):
    file_name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file_adr = models.CharField(max_length=255, verbose_name="文件地址")  # 文件地址
    big_number_name = models.CharField(max_length=255, verbose_name="大编号名")  # 大编号名
    big_number_num = models.IntegerField(default=0, verbose_name="大编号序号")  # 大编号序号
    small_number = models.IntegerField(default=0, verbose_name="小编号序号")  # 小编号序号
    production_date = models.DateField(verbose_name="制作日期")  # 制作日期
    producer = models.CharField(max_length=255, verbose_name="制作人")  # 制作人
    game_name = models.CharField(max_length=255, choices=GameTypes, verbose_name="游戏名")  # 游戏名，NSG/AOW
    content = models.CharField(max_length=255, verbose_name="系列名")  # 图片系列名
    size = models.CharField(max_length=255, choices=SizeTypes, verbose_name="尺寸")  # 尺寸,16:9/9:16/1:1
    language = models.CharField(max_length=255, choices=LanguageTypes, verbose_name="语言")  # 语言,EN/CN/JP...
    localization = models.CharField(max_length=255, choices=LocalTypes, verbose_name="本地化")  # 本地化，原版/改版/预约/立即下载
    run_state = models.CharField(max_length=255, verbose_name="数据情况")  # 跑数据情况
    consumption = models.FloatField(default=0, verbose_name="消耗量")  # 消耗量
    file_type = models.CharField(choices=FileTypes, max_length=255, verbose_name="文件类型")  # 文件类型,mp4/png
    check_people = models.CharField(default='A', max_length=20, verbose_name="检查人")  # 检查人
    remark = models.CharField(default='NONE', max_length=255, verbose_name='备注')  # 备注
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    use = models.CharField(max_length=255, choices=UseTypes, verbose_name='用途')  # 用途，广告/商店/icon
    delete_time = models.DateTimeField(verbose_name='删除时间')  # 删除时间
    delete_from = models.CharField(max_length=255, verbose_name='删除来源')  # 删除来源
    up_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')  # 上传时间
    store_mode = models.CharField(default='正常', max_length=255, verbose_name='入库模式')  # 入库模式，替换/补交/正常
    check_time = models.DateTimeField(default=timezone.now, verbose_name='审核时间')  # 审核通过时间
    reserve_a = models.CharField(max_length=255, verbose_name='备用字段1', null=True)  # 备用字段1
    reserve_b = models.CharField(max_length=255, verbose_name='备用字段2', null=True)  # 备用字段2
    reserve_c = models.CharField(max_length=255, verbose_name='备用字段3', null=True)  # 备用字段3

class Language(models.Model):
    country=models.CharField(max_length=255,verbose_name='国家')                            #国家