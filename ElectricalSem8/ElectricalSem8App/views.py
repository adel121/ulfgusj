from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.db import models
from django.utils import timezone
import datetime
from .models import Course, Video,Document,VisitCount, News, Student, Group,Viewer, Schedule
from .forms import StudentForm
from django.urls import reverse
#from .forms import ExtractAllDataForm, LoginForm,ViewDeliveryOutForm, ManagerForm,Delivery_OutForm,ViewClientForm, ViewDeliveryInForm, ClientForm, Delivery_InForm, BillForm
from datetime import date as DATE
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
mapper1 =["","Electric Machines","Microprocessor", "Instrumentation", "Data Analysis", "Telecom I", "Automatique II", "Economics", "Operating Systems", "Passive Filter Synthesis", "Communication and mini project"]
mapper = ["","Microprocessor II", "DataBase","Telecom II", "Biomedical", "Digital Processing","Automatique III", "Optoelectronics", "Operational Research", "Human Rights", "EDP"]
date = ["6/7/2021", "9/7/2021", "13/7/2021", "16/7/2021 - independence day "]
def mapping(order):
    schedule = "<ul>"
    days = order.split("+")
    i = 1
    for day in days:
        subjects = day.split(',')
        if (len(day)==0):
            continue
        schedule += "Day-"+str(i) + " (" + date[i-1] +")"
        i+=1
        for subj in subjects:
            schedule += "<li>" + mapper[int(subj)] +"</li>"
        schedule+="<hr>"
    return schedule + "</ul>"


def grades(request):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    Result = "unknown yet"
    if viewer.Total >0 and viewer.Total < 60:
        Result = "Failed"
    elif viewer.Total >0 and viewer.Total >= 60:
        Result = "Passed"
    return render(request,"grades.html",{'viewer':viewer, "Result": Result})

def vote(request):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    if request.method == "POST":
        f1 = int(request.POST.get("f1",-1))
        f2 = int(request.POST.get("f2",-1))
        f3 = int(request.POST.get("f3",-1))
        f4 = int(request.POST.get("f4",-1))
        f5 = int(request.POST.get("f5",-1))
        f6 = int(request.POST.get("f6",-1))
        f7 = int(request.POST.get("f7",-1))
        f8 = int(request.POST.get("f8",-1))
        f9 = int(request.POST.get("f9",-1))
        f10 = int(request.POST.get("f10",-1))
        f11 = int(request.POST.get("f11",-1))
        f12 = int(request.POST.get("f12",-1))
        day1 = [f1 , f2, f3]
        day2 = [f4 , f5, f6]
        day3 = [f7 , f8, f9]
        day4 = [f10, f11, f12]
        temp_days = [day1, day2, day3, day4]
        days = []
        for day in temp_days:
            day.sort()
            days.append(day)
        order = ""
        test = []
        for day in days:
            if (len(order))>0 and day[0]+day[1]+day[2] != -3:
                order = order + '+'

            for elem in day:
                if elem==-1:
                    continue
                order += str(elem) +","
                test.append(int(elem))

            if day[0]+day[1]+day[2] != -3:
                order = order[:len(order)-1]
        test.sort()
        res = ""
        for t in test:
            res += str(t) +","
        for i in range(len(test)):
            if test[i]!=int(i)+1 or len(test)!=10:
                return HttpResponse("Invalid Input, Reload the page and refill the form correctly ")

        try:
            schedule = Schedule.objects.get(Order = order)
        except:
            schedule = Schedule()
            schedule.Order = order

        schedule.Votes += 1
        if len(schedule.Order)>0:
            schedule.save()
        if len(viewer.Schedule):
            schedule=Schedule.objects.get(Order = viewer.Schedule)
            schedule.Votes -= 1
            schedule.save()
        viewer.Schedule = order
        viewer.save()





    schedules = []
    i=1
    scheds = Schedule.objects.all()
    for sched in scheds:
        schedules.append([i,sched.Votes,mapping(sched.Order)])
        i+=1
    current = "Not Specified"
    if len(viewer.Schedule)>0:
        current = mapping(viewer.Schedule)
    return render(request,"vote.html", {'viewer':viewer,'schedules':schedules, 'current':current})


# Create your views here.
def project_registration(request):
     try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
        students = Viewer.objects.all()
     except:
        return HttpResponseRedirect(reverse('viewer_login'))
     if request.method == "POST":
         data1=request.POST.get("databasetopic1",0)
         data2=request.POST.get("databasetopic2",0)
         data3=request.POST.get("databasetopic3",0)
         data4=request.POST.get("databasetopic4","unchosen")
         datamate=request.POST.get("databasegroup","unchosen")
         bio1 = request.POST.get("biomedicaltopic","unchosen")
         biomate=request.POST.get("biomedicalgroup","unchosen")
         viewer.data1=data1
         viewer.data2=data2
         viewer.data3=data3
         viewer.data4=data4
         viewer.datamate=datamate
         viewer.bio1=bio1
         viewer.biomate=biomate
         viewer.save()
         if datamate != "unchosen" and datamate != viewer.Name:
             temp_viewer= Viewer.objects.get(Name=datamate)
             temp_viewer.data1=data1
             temp_viewer.data2=data2
             temp_viewer.data3=data3
             temp_viewer.data4=data4
             temp_viewer.datamate=viewer.Name
             temp_viewer.save()
         if biomate != "unchosen" and biomate != viewer.Name:
             temp_viewer = Viewer.objects.get(Name=biomate)
             temp_viewer.bio1=bio1
             temp_viewer.biomate=viewer.Name
             temp_viewer.save()
         return HttpResponseRedirect(reverse('viewer_login'))
     return render(request, 'project_registration.html', {'viewer':viewer, 'students':students})
def separate(request):
    cnt = 0
    students = Student.objects.all()
    for student in students:
        student.LinuxGroup = "-"
        if student.Discipline == "POWER" or student.Discipline == "power" :
            continue
        if cnt <= 22:
            student.LinuxGroup = "A"
            cnt = cnt + 1
        else:
            student.LinuxGroup = "B"
        student.save()
    return HttpResponse("Mission Succeeded")

def add_group(request):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    if request.method == 'POST':
        group = Group()
        group.Names = viewer.Name + "," + request.POST.get('names',"")
        group.Week = request.POST['weekselect']
        group.Method = request.POST['methodselect']
        group.Description = request.POST.get('description',"")
        group.save()
        return HttpResponse("<div class='jumbotron container'><h1>Thank You! Your Response Has Been Recorded<h1></div>")
    else:
        return render(request, 'add_group.html',{'viewer':viewer,})

def student_details(request, Id):
    Id=int(Id)
    student = Student.objects.get( pk = Id )

    return render(request,'student_details.html', {'student':student})

def index(request):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    visit = VisitCount.objects.get( pk = 1)
    visit.Count += 1
    visit.save()
    news = News.objects.all()
    return render(request,'index.html', {'viewer':viewer,'visit_count':visit.Count, 'news':news})


class StudentCreate(CreateView):
    model = Student
    fields = '__all__'

def course_about(request, name):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    about = Course.objects.get(Name = name).About
    return render(request,'course_about.html', {'viewer':viewer,'name':name, 'about':about})


def course_list(request, discipline="telecom"):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    courses=Course.objects.all()
    return render(request, 'course_list.html', {'viewer':viewer,'courses':courses, 'discipline':discipline})

def course_prompt(request, name):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    return render(request,'course_prompt.html', {'viewer':viewer,'name':name})

def course_videos(request, name):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    videos = Video.objects.all().filter(Course=name)
    return render(request,'course_videos.html',{ 'viewer':viewer,'videos':videos , 'name':name})

def course_documents(request, name):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
    except:
        return HttpResponseRedirect(reverse('viewer_login'))
    documents = Document.objects.all().filter(Course=name)
    siz = documents.count()
    data = dict()
    for  i in range(1,siz+1):
        data[i]=documents[i-1]
    return render(request,'course_documents.html',{'viewer':viewer,'data':data, 'name':name, })

def viewer_login(request, logged_out=0):
    try:
        pk = request.session['viewer_id']
        viewer = Viewer.objects.get(pk=pk)
        return HttpResponseRedirect(reverse('index',args=()))
    except:
        pass
    message =""
    if logged_out==1:
        message = "You were Successfully, log-in if desired :)"
    if request.method == 'POST':
        username = request.POST.get("username", "noname")
        password = request.POST.get("password", "nopassword")
        try:
            viewer = Viewer.objects.get(Username = username)
            if password == viewer.Password:
                request.session['viewer_id']=viewer.pk
                return HttpResponseRedirect(reverse('index',args=()))
            else:
                message = "Failed"
        except:
            message = "Failed"

    return render(request, "viewer_login.html", {"message":message})

def viewer_logout(request):
    try:
        del request.session['viewer_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('viewer_login', args=(1,)))