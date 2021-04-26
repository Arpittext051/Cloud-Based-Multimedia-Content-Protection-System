from django.shortcuts import render,redirect
from .forms import CustomerRegistraitonForm,LoginForm
from django.views import View
from django.contrib import messages
from .models import *
import datetime
import os.path


# Create your views here.
# def login(request):
#     return render(request, 'Login.html')

# def register(request):
#     return render(request, 'register.html')

class CustomerRegistraitonView(View):
    def get(self,request):
        form = CustomerRegistraitonForm()
        return render(request, 'register/register.html',{'forms':form})

    def post(self,request):
        form = CustomerRegistraitonForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations... You succesufully registered ')
            form.save()
        return render(request, 'register/register.html',{'forms':form})


def changepass(request):
    return render(request, 'changepassword.html')


def homepage(request):
    return render(request, 'homepage/homepage.html')



def media(request):
    if request.method == "POST":
        print(request.FILES.get('file1'))
        if os.path.exists("media/multimedia/"+str(request.FILES.get('file1'))):
           
            messages.error(request,'File Already Exists You Are Entering Dublicate Files ')
            return redirect("media")
        else:
            up = Upload()
            user = request.user
            date = datetime.datetime.today()
            up.user = user
            up.option = request.POST['option']
            up.file1 = request.FILES.get('file1')
            up.date = date
            up.save()
            messages.success(request,'Congratulations... Your File  succesufully Uploaded ')
            return redirect("media")
    return render(request, "media/media.html")


def history(request):
    his = Upload.objects.filter(user = request.user , date=datetime.datetime.today() ).order_by("-id")
    return render(request,"history.html",{"his":his})

def multimedia(request):
    his = Upload.objects.filter(user = request.user).order_by("-id")
    return render(request, "multimedia.html",{'his':his})