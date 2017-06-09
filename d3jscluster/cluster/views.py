#!/usr/bin/python2.7
# -*- coding: utf-8 -*-  
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse
from d3jscluster import settings
from models import Tel2Addr,RewardRecord,RewardActivity
from rewardprocess import *
import os
import json
# Create your views here.

def d3_cluster(request):
    t = loader.get_template('cluster.html')
    with open("china.json") as rootfile:
        data = json.load(rootfile)
        jsondata = json.dumps(data,ensure_ascii=False,indent=4)
        return HttpResponse(t.render({'rootfile':jsondata,}))

def geomap(request):
    t = loader.get_template("geochina.html")
    return HttpResponse(t.render())

def heatmap(requst):
    t = loader.get_template("heatMap.html")
    return HttpResponse(t.render())


def home(request):
    t=loader.get_template('index.html')
    html=t.render(Context({
        "title":"home",
        "static_dir":settings.STATIC_DIRS

        }))
    return HttpResponse(html)

#上传奖励表
def uploadreward(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            return HttpResponse("no files for upload!")  
        destination = open(os.path.join(settings.UPLOAD_DIR,request.POST.get("reward_huodong_name")+".xls"),'wb+')    # 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close() #关闭文件 
        activity = RewardActivity(request.POST.get("reward_huodong_name"),
                                request.POST.get("reward_cmake"),
                                request.POST.get("reward_huodong_name")+".xls")

        filepath = os.path.join(settings.UPLOAD_DIR,request.POST.get("reward_huodong_name")+".xls")
        checkthread = CheckThread(filepath)
        checkthread.start()
        return HttpResponse("upload over!")  
    pass

#处理奖励表数据
def processreward(request):
    pass

#项目主页
def realreward(request):
    if request.method == "POST": 
        uploadreward(request)
    return render_to_response('index.html',{})

#校验上传后处理log
def get_rewardcheck_log(request):
    return HttpResponse("处理中，请稍后！") 
    pass

def test(request):
    checkThread = CheckThread("hehe")
    print "thread start"
    checkThread.start()
    print "thread start2"
    return HttpResponse("heheheh")




def staticcheck_runlog(request):
    curip = request.META['REMOTE_ADDR']
    username = request.user.first_name
    userid = request.user.username
    logfile_url = "http://heheh/log/lpccheck_%s.log" % (userid)
    #return HttpResponse(logfile_url)
    try:
        data = urllib2.urlopen(logfile_url).read()
    except:
        data = ""
    serlog_list = data.split("\n")
    serlog = ""
    num = 1
    for line in serlog_list:
        line = line.decode('gbk').encode('utf-8')
        if "[ERROR]" in line:
            serlog += "<li style=\"color:#EE0000\">" + str(num) + ":" + line + "</li>"
        elif "[DEBUG]" in line:
            serlog += "<li style=\"color:#7D26CD\">" + str(num) + ":" + line + "</li>"
        else:
            serlog += "<li style=\"color:#008B8B\">" + str(num) + ":" + line + "</li>"
        num = num + 1
    return HttpResponse(serlog)


def staticcheck_simulate_check(request):
     curip = request.META['REMOTE_ADDR']
     username = request.user.first_name
     userid = request.user.username

     if len(request.POST) < 1:
        return render_to_response('static_check/static_check_simulate.html', {"userid":userid},context_instance = RequestContext(request))

     if len(request.POST) == 1:
         optype = request.POST.get("optype")
         if optype == "netlist":
            slist_url="http://hehe?"+userid+"+"+optype
            data = urllib2.urlopen(slist_url).read()
            return HttpResponse(data)
         elif optype == "netclear":
            slist_url="http://hehe?"+userid+"+"+optype
            data = urllib2.urlopen(slist_url).read()
            return HttpResponse(data)
         else:
            return HttpResponse("未知的操作类型,请确认!")
     elif len(request.POST) == 4:
         #静态代码检查参数
         s_branch = request.POST.get("s_branch")
         s_datelist = request.POST.get("s_date").split("-")
         s_date = s_datelist[0]+"_"+s_datelist[1]+"_"+s_datelist[2]
         check_path = request.POST.get("check_path")
         check_type = request.POST.get("check_type")
         
         if s_branch == "trunk":
             check_branch = "trunk"
         elif s_branch == "release":
             check_branch = "release/rel_%s" % (s_date)
         elif s_branch == "test":
             check_branch = "test/test_%s" % (s_date)
         elif s_branch == "test2":
             check_branch = "test/test2_%s" % (s_date)
         elif s_branch == "test3":
             check_branch = "test/test3_%s" % (s_date)
         elif s_branch == "shiwan":
             check_branch = "branch/shiwan_%s" % (s_date)
         else:
             check_branch = "trunk"

         if check_branch == None or check_path == None:
            return HttpResponse("不能为空")
         slist_url = "http://heheh/check_ctrl.sh?%s+%s+%s+%s+%s" % (check_branch,check_path,userid,"week_check",check_type)
         print "week_check=",slist_url
         data = urllib2.urlopen(slist_url)
         return HttpResponse("send branch cmd ok")
     else:
        return render_to_response('static_check/static_check_simulate.html', {"userid":userid},context_instance = RequestContext(request))

