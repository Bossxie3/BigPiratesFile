import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from TestModel.models import File,User,Language
from django.db.models import Q
import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import os
import webbrowser

#获取明天    
def tomorrow_get(d):
    dayscount = datetime.timedelta(days=-1)
    dayto = d - dayscount
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return date_to

def Split_num_letters(astr):
    nums, letters = "", ""

    for i in astr:

        if i.isdigit():
            nums = nums + i
        elif i.isspace():
            pass
        else:
            letters = letters + i
    return nums, letters

# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'searchContent' in request.GET and request.GET['searchContent']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

def link_youtube(request):
    DEVELOPER_KEY = 'AIzaSyD-TfTjLUGR6o6i4S_4v0hpLP5t4HTkY0U'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    print('1111')
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q='Ubuntu',
        part='id,snippet',
        maxResults=3
    ).execute()
    print(search_response)
    return render(request, 'supple.html', locals())

# 接收POST请求数据
def search_post(request):
    #获取查询条件
    filename = request.POST['filename']
    gameName=request.POST.get('gameName')
    startDate=request.POST.get('startDate')
    endDate = request.POST.get('endDate')
    bigNumbername=request.POST.get('bigNumbername')
    producers=request.POST.get('producers')
    makeMode=request.POST.get('makeMode')
    language=request.POST.get('language')
    localization=request.POST.get('localization')
    checkPeople=request.POST.get('checkPeople')
    users=User.objects.all()
    languages=Language.objects.all()
    #定义存储查询条件的字典
    search_dict=dict()
    BigNumber=Split_num_letters(bigNumbername)
    #获取明天日期
    inputEndDate=endDate.split('-')
    nextDay=datetime.datetime(int(inputEndDate[0]), int(inputEndDate[1]), int(inputEndDate[2]), 00, 00, 00)
    nextDay = (nextDay + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    if BigNumber[0]=='':
            print('kong!')
            all_date = File.objects.filter(
                Q(file_name__icontains=filename) & Q(big_number_name__icontains=BigNumber[1])  & Q(producer__icontains=producers) & Q(
                    make_mode__icontains=makeMode) & Q(language__icontains=language) & Q(
                    localization__icontains=localization)& Q(check_people__icontains=checkPeople) & Q(game_name__icontains=gameName))
    else:
        all_date=File.objects.filter(Q(file_name__icontains=filename)&Q(big_number_name__icontains=BigNumber[1])&Q(big_number_num=BigNumber[0])&Q(producer__icontains=producers)&Q(make_mode__icontains=makeMode)&Q(language__icontains=language)&Q(localization__icontains=localization)
        &Q(game_name__icontains=gameName)& Q(checkPeople__icontains=checkPeople))
    if startDate and endDate:
        all_date=all_date.filter(Q(up_time__gte=startDate)&Q(up_time__lte=nextDay))
    file_list=all_date
    return render(request,'show_list.html',locals())

def cache_search(request):
    return render(request)

def open_File(request):
    if request.method=='GET':
        return render(request,'base.html')

def open_FileII(request):
    if request.method=='GET':
        path=request.GET.get('adr')
        webbrowser.open('http://www.baidu.com')
        #os.startfile(path+'\\100_1_2021.08.30_马业飞_NSG_布莱克场景展示_16B9_剪辑_VN.mp4')
        #os.system(r"start " + 'Z:\TestStore/2.png')
        return render(request,'base.html')