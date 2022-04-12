from django.contrib import admin
from .models import File

# Register your models here.
#admin.site.register(File)

class FileManager(admin.ModelAdmin):
    #列表页显示哪些字段的列
    list_display = ['id','file_name','big_number_name','big_number_num','small_number','production_date','producer','make_mode','language','game_name','size']
    #控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['file_name']
    #添加过滤器
    list_filter = ['big_number_name']
    #添加搜索框[模糊查询]
    search_fields = ['file_name','big_number_name']
    #添加可在列表页编辑的字段
    list_editable = ['big_number_num']

admin.site.register(File,FileManager)
