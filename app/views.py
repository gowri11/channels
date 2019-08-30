from django.shortcuts import render,redirect
from .forms import Registration
from .forms import login,ChannelForm
from .models import Register,Dishes
# from django.core.mail import send_mail
from django.http import HttpResponse

from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError,EmailMessage
# Create your views here.

def Email_Sending(request,email):
    To=email
    From='sekharpajjuri'
    Sub='regardng Eamcet concelling'
    Message='you selectd'
    try:
        mail = EmailMessage(Sub,From,Message,[To,])
#mail.attach(File_Attach.name, File_Attach.read(),File_Attach.content_type)
        mail.send()
        return HttpResponse('send')
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

def getregistration(request):
    form=Registration()
    if request.method=='POST':
        form=Registration(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            area=form.cleaned_data['area']
            city=form.cleaned_data['city']
            email=form.cleaned_data['email']
            #email1=request.POST.get('email','')
            mobile=form.cleaned_data['mobile']
            rf=Register(name=name,area=area,city=city,email=email,mobile=mobile)
            rf.save()
            return redirect(Email_Sending,email)
    return render(request,'register.html',{'form':form})


def getlogin(request):
    form=login()
    if request.method=='POST':
        form=login(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            mobile=form.cleaned_data['mobile']
            gl=Register.objects.filter(name=name,mobile=mobile)
            if not gl:
                return HttpResponse("login fail")
            else:
                return render(request,"home.html")
    return render(request,'login.html',{'form':form})

def channelform(request):
    form=ChannelForm()
    if request.method=='POST':
       form=ChannelForm(request.POST)
       form.save()
    return render(request,'airtel.html',{'form':form})

def dishform(request):
    form=ChannelForm()
    if request.method=='POST':
       form=ChannelForm(request.POST)
       form.save()
    return render(request,'dish.html',{'form':form})

def tataform(request):
    form=ChannelForm()
    if request.method=='POST':
       form=ChannelForm(request.POST)
       form.save()
    return render(request,'tata.html',{'form':form})

def sunform(request):
    form=ChannelForm()
    if request.method=='POST':
       form=ChannelForm(request.POST)
       form.save()
    return render(request,'sun.html',{'form':form})

# def channelform(request):
#     form=ChannelForm()
#     if request.method=='POST'
#        form=ChannelForm(request.POST)
#        form.save()
#     return render(request,'tata.html',{'form':form})

# def pricelimit(request):

