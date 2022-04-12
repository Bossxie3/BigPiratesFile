import os

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from TestModel.models import File,CacheFile,User,SuppleFile,PicFile,CachePicFile,SupplePicFile,BigNumber,DeleteFile,DeletePicFile,Language
from django.contrib import  admin
from django.db.models import Q
from django.views.decorators import csrf
from ftplib import FTP
from django.forms.models import model_to_dict
import hashlib
import time
import datetime

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

#获取当前日期的前一周
def week_get(d):
    dayscount = datetime.timedelta(days=7)
    print(dayscount)
    dayto = d - dayscount
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return date_to

def anyday_get(d,somedays):
    dayscount = datetime.timedelta(days=somedays)
    print(dayscount)
    dayto = d - dayscount
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return date_to

#获取明天    
def tomorrow_get(d):
    dayscount = datetime.timedelta(days=-1)
    dayto = d - dayscount
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return date_to    

#退出登录
def logout_view(request):
    #删除session值
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    #删除Cookies
    resp=HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp

def check_login(fn):
    def wrap(request,*args,**kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            #检查Cookies
            c_username=request.COOKIES.get('username')
            c_uid=request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/login')
            else:
                #回写session
                request.session['username']=c_username
                request.session['uid']=c_uid
        return  fn(request,*args,**kwargs)
    return wrap

'''def hello(request):
    return render(request,'hello.html')'''

#主页显示
def index_view(request):
    if request.method=='GET':
        nowDate=datetime.datetime.now()
        startDay=anyday_get(nowDate,1)
        startDay=startDay.strftime('%Y-%m-%d')
        nowDate = nowDate.strftime('%Y-%m-%d')
        c_username = request.session.get('username')
        bignumbers=BigNumber.objects.filter(small_number=0,big_number_name='通常')
        delete_files=DeleteFile.objects.filter(Q(delete_from='已入库') & Q(check_people=c_username) & Q(delete_time__gte=startDay) & Q(delete_time__lte=nowDate))
        replace_files=DeleteFile.objects.filter(Q(delete_from='替换') & Q(delete_time__gte=startDay) & Q(delete_time__lte=nowDate))
        print(replace_files)
        dic={}
        num=0
        #dic=model_to_dict(replace_files)
        for file in replace_files:
            dic[num]=model_to_dict(file)
            num+=1
        print('转换后：')
        Country=[]
        length=len(dic)
        print(length)
        for l in range(length):
            if l in dic:
                nation=dic[l]['language']
                Country.append('%s' % (nation))
                for j in range(length):
                    if j in dic:
                        if(l!=j):
                            if nation==dic[j]['language']:
                                del dic[j]
        print(Country)
        return render(request,'index/index.html',locals())

#删除视频文件显示
def delete_file(request):
    if request.method=='GET':
        c_username = request.session.get('username')
        now = datetime.datetime.now()
        lastweek = week_get(now)
        endDate = now.strftime('%Y-%m-%d')
        now = tomorrow_get(now)
        lastweekDate = lastweek.strftime('%Y-%m-%d')
        now = now.strftime('%Y-%m-%d')
        startDate = lastweekDate
        delete_files = DeleteFile.objects.filter(Q(delete_time__gte=startDate) & Q(delete_time__lte=now)).order_by('-delete_time')
        return render(request,'delete_file.html',locals())
    elif request.method == 'POST':
        # 获取查询条件
        c_username = request.session.get('username')
        filename = request.POST['filename']
        gameName = request.POST.get('gameName')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        bigNumbername = request.POST.get('bigNumbername')
        producers = request.POST.get('producers')
        makeMode = request.POST.get('makeMode')
        language = request.POST.get('language')
        localization = request.POST.get('localization')
        deleteFrom = request.POST.get('deleteFrom')
        # 定义存储查询条件的字典
        search_dict = dict()
        # bigNumber=Split_num_letters(bigNumbername)
        # 如果查询条件不为空就写入到字典中
        BigNumber = Split_num_letters(bigNumbername)
        inputEndDate = endDate.split('-')
        nextDay = datetime.datetime(int(inputEndDate[0]), int(inputEndDate[1]), int(inputEndDate[2]), 00, 00, 00)
        nextDay = (nextDay + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        all_date = DeleteFile.objects.filter(
            Q(file_name__icontains=filename) & Q(big_number_name__icontains=BigNumber[1]) & Q(
                big_number_num__icontains=BigNumber[0]) & Q(producer__icontains=producers) & Q(
                make_mode__icontains=makeMode) & Q(language__icontains=language) & Q(
                localization__icontains=localization) & Q(
                delete_from__icontains=deleteFrom)
            & Q(game_name__icontains=gameName))

        if startDate and endDate:
            all_date = all_date.filter(Q(delete_time__gte=startDate) & Q(delete_time__lte=nextDay))

        delete_files = all_date
        return render(request,'delete_file.html',locals())

#删除图片文件显示
def delete_picfile(request):
    if request.method=='GET':
        c_username = request.session.get('username')
        now = datetime.datetime.now()
        lastweek = week_get(now)
        endDate = now.strftime('%Y-%m-%d')
        now = tomorrow_get(now)
        lastweekDate = lastweek.strftime('%Y-%m-%d')
        now = now.strftime('%Y-%m-%d')
        startDate = lastweekDate
        delete_files = DeletePicFile.objects.filter(Q(delete_time__gte=startDate) & Q(delete_time__lte=now)).order_by('-delete_time')
        return render(request,'delete_picfile.html',locals())
    elif request.method == 'POST':
        # 获取查询条件
        filename = request.POST['filename']
        gameName = request.POST.get('gameName')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        bigNumbername = request.POST.get('bigNumbername')
        producers = request.POST.get('producers')
        use = request.POST.get('use')
        language = request.POST.get('language')
        localization = request.POST.get('localization')
        c_username = request.session.get('username')
        deleteFrom = request.POST.get('deleteFrom')
        # 定义存储查询条件的字典
        search_dict = dict()
        # bigNumber=Split_num_letters(bigNumbername)
        # 如果查询条件不为空就写入到字典中
        BigNumber = Split_num_letters(bigNumbername)
        inputEndDate = endDate.split('-')
        nextDay = datetime.datetime(int(inputEndDate[0]), int(inputEndDate[1]), int(inputEndDate[2]), 00, 00, 00)
        nextDay = (nextDay + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        all_date = DeletePicFile.objects.filter(
            Q(file_name__icontains=filename) & Q(big_number_name__icontains=BigNumber[1]) & Q(
                big_number_num__icontains=BigNumber[0]) & Q(producer__icontains=producers) & Q(
                use__icontains=use) & Q(language__icontains=language) & Q(
                localization__icontains=localization)
            & Q(game_name__icontains=gameName)& Q(
                delete_from__icontains=deleteFrom))

        if startDate and endDate:
            all_date = all_date.filter(Q(delete_time__gte=startDate) & Q(delete_time__lte=nextDay))

        delete_files = all_date
        return render(request,'delete_picfile.html',locals())

def reg_view(request):
    #注册
    if request.method == 'GET':
        # GET    返回页面
        return  render(request,'user/register.html')
    elif request.method == 'POST':
        # POST   处理提交数据
        username=request.POST['username']
        password_1=request.POST['password_1']
        password_2=request.POST['password_2']
    #   1，两个密码要保持一致
    if password_1 != password_2:
        return HttpResponse('两次密码输入不一致')
    #哈希算法 - 给定明文，计算出一段定长的，不可逆的值；md5，sha-256
    #特点
    # 1，定长输出： 不管明文输入长度为多少，哈希值都是定长的，md5 - 32位16进制
    # 2，不可逆： 无法反向计算出 对应的 明文
    # 3，雪崩效应： 输入改变，输出必然变
    #场景：1，密码处理 2，文件完整性校验
    #如何使用
    m=hashlib.md5()
    m.update(password_1.encode())
    password_m=m.hexdigest()

    #   2，当前用户名是否可用
    old_users=User.objects.filter(username=username)
    if old_users:
        return  HttpResponse('用户名已注册')
    #   3，插入数据[明文处理密码]
    try:
        user = User.objects.create(username=username,password=password_m)
    except Exception as e:
        # 有可能 报错 - 重复插入 [唯一索引注意并发写入问题]
        print('--create user error %s'%(e))
        return HttpResponse('用户名已注册')

    #免登录一天
    request.session['username']=username
    request.session['uid']=user.id
    #TODO 修改session存储时间为1天

    return HttpResponseRedirect('/index')

def login_view(request):
    if request.method == 'GET':
        #获取登录界面
        #检测登录状态，如果登录了，显示'已登录'
        if request.session.get('username') and request.session.get('uid'):
            #return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        #检查Cookies
        c_username=request.COOKIES.get('username')
        c_uid=request.COOKIES.get('uid')
        if c_username and c_uid:
            #回写session
            request.session['username']=c_username
            request.session['uid']=c_uid
            #return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        return render(request,'user/login.html')
    elif request.method == 'POST':
        #处理数据
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('用户名或密码错误')

        #比对密码
        m = hashlib.md5()
        m.update(password.encode())

        if m.hexdigest() != user.password:
            return  HttpResponse('用户名或密码错误')

        #记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        resp=HttpResponseRedirect('/index')
        #判断用户是否 点选了 ‘记住用户名’
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24*3)
            resp.set_cookie('uid',user.id,3600*24*3)
        #点选了 -> Cookies 存储 username，uid 时间3天
        return resp

#转换器示例
def pagen_view(request,pg):
    html='这个编号为%s的网页'%(pg)
    return HttpResponse(html)

def filelist(request):
    return render(request,'base.html')

@check_login
def pic_upload(request):
    if request.method=='GET':
        c_username = request.session.get('username')
        print(c_username)
        file_list = CachePicFile.objects.filter(check_people=c_username)
        context = {'file_list': file_list}
        return render(request, 'picupload.html', context)

#图片检索，显示一周内的数据
def show_picture(request):
    if request.method=='GET':
        now=datetime.datetime.now()
        lastweek=week_get(now)
        endDate=now.strftime('%Y-%m-%d')
        now=tomorrow_get(now)
        lastweekDate=lastweek.strftime('%Y-%m-%d')
        now=now.strftime('%Y-%m-%d')
        startDate=lastweekDate
        file_list=PicFile.objects.filter(Q(up_time__gte=startDate)&Q(up_time__lte=now)).order_by('-up_time')
        return render(request,'show_picture.html',locals())
    elif request.method=='POST':
        # 获取查询条件
        filename = request.POST['filename']
        gameName = request.POST.get('gameName')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        bigNumbername = request.POST.get('bigNumbername')
        producers = request.POST.get('producers')
        use = request.POST.get('use')
        language = request.POST.get('language')
        localization = request.POST.get('localization')
        # 定义存储查询条件的字典
        search_dict = dict()
        # bigNumber=Split_num_letters(bigNumbername)
        # 如果查询条件不为空就写入到字典中
        BigNumber = Split_num_letters(bigNumbername)
        # 获取明天日期
        # inputEndDate=endDate.split('-')
        # nextDay=datetime.datetime(int(inputEndDate[0]), int(inputEndDate[1]), int(inputEndDate[2]), 00, 00, 00)
        # nextDay = (nextDay + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        if BigNumber[0]=='':
            all_date = PicFile.objects.filter(
                Q(file_name__icontains=filename) & Q(big_number_name__icontains=BigNumber[1])  & Q(producer__icontains=producers) & Q(
                    use__icontains=use) & Q(language__icontains=language) & Q(
                    localization__icontains=localization)
                & Q(game_name__icontains=gameName))
        else:
            all_date = PicFile.objects.filter(
                Q(file_name__icontains=filename) & Q(big_number_name__icontains=BigNumber[1]) & Q(big_number_num=BigNumber[0]) & Q(producer__icontains=producers) & Q(
                    use__icontains=use) & Q(language__icontains=language) & Q(
                    localization__icontains=localization) & Q(game_name__icontains=gameName))
        if startDate and endDate:
            all_date = all_date.filter(Q(up_time__gte=startDate) & Q(up_time__lte=endDate))

        # file_list=File.objects.filter(production_date__range=(start_date,end_date))
        # context={'file_list':all_date}
        file_list = all_date
        # print(context)
        # for file in file_list:
        # file.file_name=file
        return render(request, 'show_picture.html', locals())

#默认检索界面，显示一周内数据
def show_list(request):
    now=datetime.datetime.now()
    lastweek=week_get(now)
    endDate=now.strftime('%Y-%m-%d')
    now=tomorrow_get(now)
    lastweekDate=lastweek.strftime('%Y-%m-%d')
    now=now.strftime('%Y-%m-%d')
    startDate=lastweekDate
    file_list=File.objects.filter(Q(up_time__gte=startDate)&Q(up_time__lte=now)).order_by('-check_time')
    users=User.objects.all()
    languages=Language.objects.all()
    return render(request,'show_list.html',locals())

@check_login
def supple(request):
    if request.method == 'GET':
        c_username=request.session.get('username')
        print(c_username)
        file_list=SuppleFile.objects.filter(check_people=c_username)
        now = datetime.datetime.now()
        lastweek = week_get(now)
        endDate = now.strftime('%Y-%m-%d')
        now = tomorrow_get(now)
        lastweekDate = lastweek.strftime('%Y-%m-%d')
        now = now.strftime('%Y-%m-%d')
        startDate = lastweekDate
        searchfile_list = File.objects.filter(Q(up_time__gte=startDate) & Q(up_time__lte=now)).order_by('-big_number_num')
        return render(request,'supple.html',locals())
    elif request.method == 'POST':
        c_username=request.session.get('username')
        print(c_username)
        file_list=SuppleFile.objects.filter(check_people=c_username)
        # 获取查询条件
        filename = request.POST['filename']
        gameName = request.POST.get('gameName')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        bigNumbername = request.POST.get('bigNumbername')
        producers = request.POST.get('producers')
        makeMode = request.POST.get('makeMode')
        language = request.POST.get('language')
        localization = request.POST.get('localization')
        # 定义存储查询条件的字典
        search_dict = dict()
        # bigNumber=Split_num_letters(bigNumbername)
        # 如果查询条件不为空就写入到字典中
        BigNumber = Split_num_letters(bigNumbername)
        inputEndDate = endDate.split('-')
        nextDay = datetime.datetime(int(inputEndDate[0]), int(inputEndDate[1]), int(inputEndDate[2]), 00, 00, 00)
        nextDay = (nextDay + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        all_date = File.objects.filter(
            Q(file_name__icontains=filename) & Q(big_number_name__icontains=BigNumber[1]) & Q(
                big_number_num__icontains=BigNumber[0]) & Q(producer__icontains=producers) & Q(
                make_mode__icontains=makeMode) & Q(language__icontains=language) & Q(
                localization__icontains=localization)
            & Q(game_name__icontains=gameName))

        if startDate and endDate:
            all_date = all_date.filter(Q(up_time__gte=startDate) & Q(up_time__lte=nextDay))

        searchfile_list = all_date
        return render(request,'supple.html',locals())

@check_login
def pic_supple(request):
    if request.method == 'GET':
        c_username=request.session.get('username')
        print(c_username)
        file_list=SupplePicFile.objects.filter(check_people=c_username)
        now = datetime.datetime.now()
        lastweek = week_get(now)
        endDate = now.strftime('%Y-%m-%d')
        now = tomorrow_get(now)
        lastweekDate = lastweek.strftime('%Y-%m-%d')
        now = now.strftime('%Y-%m-%d')
        startDate = lastweekDate
        searchfile_list = PicFile.objects.filter(Q(up_time__gte=startDate) & Q(up_time__lte=now)).order_by('-big_number_num')
        return render(request,'pic_supple.html',locals())
    elif request.method == 'POST':
        c_username=request.session.get('username')
        print(c_username)
        file_list=SupplePicFile.objects.filter(check_people=c_username)
        # 获取查询条件
        filename = request.POST['filename']
        gameName = request.POST.get('gameName')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        bigNumbername = request.POST.get('bigNumbername')
        producers = request.POST.get('producers')
        use = request.POST.get('use')
        language = request.POST.get('language')
        localization = request.POST.get('localization')
        # 定义存储查询条件的字典
        search_dict = dict()
        # bigNumber=Split_num_letters(bigNumbername)
        # 如果查询条件不为空就写入到字典中
        BigNumber = Split_num_letters(bigNumbername)
        inputEndDate = endDate.split('-')
        nextDay = datetime.datetime(int(inputEndDate[0]), int(inputEndDate[1]), int(inputEndDate[2]), 00, 00, 00)
        nextDay = (nextDay + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        all_date = PicFile.objects.filter(
            Q(file_name__icontains=filename) & Q(big_number_name__icontains=BigNumber[1]) & Q(
                big_number_num__icontains=BigNumber[0]) & Q(producer__icontains=producers) & Q(
                use__icontains=use) & Q(language__icontains=language) & Q(
                localization__icontains=localization)
            & Q(game_name__icontains=gameName))

        if startDate and endDate:
            all_date = all_date.filter(Q(up_time__gte=startDate) & Q(up_time__lte=nextDay))

        searchfile_list = all_date
        return render(request,'pic_supple.html',locals())

#补交界面默认显示
# @check_login
# def supple(request):
#     if request.method='GET':
#         c_username=request.session.get('username')
#         print(c_username)
#         file_list=CacheFile.objects.filter(check_people=c_username)
#         context={'file_list':file_list}
#         return render(request,'supple.html',locals())
    # elif request.method == 'POST':
    #     c_username=request.session.get('username')
    #     file_list=CacheFile.objects.filter(check_people=c_username)
    #     filename = request.POST['filename']
    #     gameName=request.POST.get('gameName')
    #     startDate=request.POST.get('startDate')
    #     endDate = request.POST.get('endDate')
    #     bigNumbername=request.POST.get('bigNumbername')
    #     producers=request.POST.get('producers')
    #     makeMode=request.POST.get('makeMode')
    #     language=request.POST.get('language')
    #     localization=request.POST.get('localization')
    #     #定义存储查询条件的字典
    #     search_dict=dict()
    #     #bigNumber=Split_num_letters(bigNumbername)
    #     #如果查询条件不为空就写入到字典中
    #     BigNumber=Split_num_letters(bigNumbername)
    
    #     all_date=File.objects.filter(Q(file_name__icontains=filename)&Q(big_number_name__icontains=BigNumber[1])&Q(big_number_num__icontains=BigNumber[0])&Q(producer__icontains=producers)&Q(make_mode__icontains=makeMode)&Q(language__icontains=language)&Q(localization__icontains=localization)
    #     &Q(game_name__icontains=gameName))

    #     if startDate and endDate:
    #         all_date=all_date.filter(Q(production_date__gte=startDate)&Q(production_date__lte=endDate))
    #     searchfile_list=all_date
    #     return render(request,'supple.html',locals())

@check_login
def file_upload(request):
    c_username=request.session.get('username')
    print(c_username)
    file_list=CacheFile.objects.filter(check_people=c_username)
    context={'file_list':file_list}
    return render(request,'upload.html',context)

#文件上传保存到markerting
def file_save(request):
    file=request.FILES['newFile']
    localFilename='//192.168.0.192/marketing/FileUpload/'
    filename='%s%s' % (localFilename,file.name)
    with open(filename,'wb') as f:
        for ffile in file.chunks():
            f.write(ffile)
    return HttpResponse('上传成功')

def file_delete(request):
    length=request.GET.get('length')
    file_list=CacheFile.objects.all()
    context={'file_list':file_list}
    return render(request,'upload.html',context)

def file_suppleStore(request):
    length=request.GET.get('length')
    print('111')
    file_list=CacheFile.objects.all()
    context={'file_list':file_list}
    return render(request,'upload.html',context)

#点击入库，删除缓存文件及缓存表相应数据，添加文件到对应位置并保存到数据库文件表
def file_store(request):
    id=request.GET.get('allData')                            #获取所有数据
    length=request.GET.get('length')            #获取长度
    leng=int(length)
    file_list=CacheFile.objects.all()
    context={'file_list':file_list}
    return render(request,'upload.html',context)
    '''path=request.GET                            #获取所有数据
    length=request.GET.get('length')            #获取长度
    leng=int(length)
    print(path)
    print(leng)
    name=[]
    for len in range(leng):
       name.append(path['allData['+str(len)+'][fileName]'])
    for len in range(leng):
        CacheFile.objects.filter(file_name=name[len]).delete()
    file_list=CacheFile.objects.all()
    context={'file_list':file_list}
    return render(request,'upload.html',context)'''
    '''ftpInstance = FTP();
    path=request.GET                            #获取所有数据
    length=request.GET.get('length')            #获取长度
    leng=int(length)
    name=[]
    for len in range(leng):
       name.append(path['allData['+str(len)+'][fileName]'])
    print('some date:')
    print(name)
    CacheFilename = '//192.168.0.192/marketing/FileUpload/'
    StoreFilename='//192.168.0.192/marketing/TestStore/'
    Cachefile=[]
    Storefile=[]
    for len in range(leng):
        Cachefile.append('%s%s' % (CacheFilename,name[len]))
        Storefile.append('%s%s' % (StoreFilename,name[len]))
    print('file name:')
    print(Cachefile)
    for len in range(leng):
        file=os.listdir(CacheFilename)
        print('file :')
        print(file)
        os.chdir(StoreFilename)
        os.rename(Cachefile[len],Storefile[len])'''
