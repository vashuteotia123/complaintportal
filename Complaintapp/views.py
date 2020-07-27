from django.shortcuts import render
from Complaintapp.forms import InfoForm
from Complaintapp.models import WardenInfo,ComplaintInfo
from django.contrib import messages

def base(request):
    return render(request,'Complaintapp/base.html')

def HomePage(request):
    return render(request,'Complaintapp/homepage.html')

def About(request):
    return render(request,'Complaintapp/about.html')

def Warden(request):
    img = WardenInfo.objects.all()
    return render(request,'Complaintapp/warden.html',{"img":img})

def SuccessComplaint(request):
    return render(request,'Complaintapp/successcomplaint.html')


def Info(request):
    form=InfoForm()
    if request.method=='POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'HII')
            return SuccessComplaint(request)
        else:
            print("error")
    return render(request,'Complaintapp/information.html',{'form':form})

def Details(request):
    complaints=ComplaintInfo.objects.all()
    mydict={'mycomplaints':complaints}
    return render(request,'Complaintapp/complaintdetails.html',context=mydict)
