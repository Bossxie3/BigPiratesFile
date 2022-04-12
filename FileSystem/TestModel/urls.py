from django.conf.urls import url
from django.urls import path
from TestModel import views,search


urlpatterns=[
    #职位列表
    path('base/',views.filelist,name='base'),
    path('show_list/',views.show_list,name='show_list'),
    path('search_post/',search.search_post,name='search_post'),
    path('open_File/',search.open_File,name='open_File'),
    path('open_FileII/',search.open_FileII,name='open_FileII'),
    path('upload/',views.file_upload,name='file_upload'),
    path('file_save/',views.file_save,name='file_save'),
    path('file_store/',views.file_store,name='file_store'),
    path('file_delete/',views.file_delete,name='file_delete'),
    path('file_suppleStore/',views.file_suppleStore,name='file_suppleStore'),
    path('page/<int:pg>',views.pagen_view),
    path('reg/',views.reg_view,name='reg'),
    path('login/',views.login_view,name='login'),
    path('index/',views.index_view,name='index'),
    path('logout/',views.logout_view,name='logout'),
    path('supple/',views.supple,name='supple'),
    path('show_picture/',views.show_picture,name='show_picture'),
    path('pic_upload/',views.pic_upload,name='pic_upload'),
    path('pic_supple/',views.pic_supple,name='pic_supple'),
    path('delete_file/',views.delete_file,name='delete_file'),
    path('delete_picfile/', views.delete_picfile, name='delete_picfile'),
    path('link_youtube/',search.link_youtube,name='link_youtube')
]