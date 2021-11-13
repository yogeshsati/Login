

from django.shortcuts import render
from Login.models import Newuser
from django.contrib import messages

def indexpage(request):
    return render(request,'index.html')

def Userreg(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Pwd=request.POST['Pwd']
        Age=request.POST['Age']
        Gender=request.POST['Gender']
        Newuser(Username=Username,Email=Email,Pwd=Pwd,Age=Age,Gender=Gender).save()
        messages.success(request,'The New User'+request.POST['Username']+ "Is saved Successfully")
        return render(request,'registration.html')
    else:
        return render(request,'registration.html')

def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'],Pwd=request.POST['Pwd'])
            print("Usernsme=",Userdetails)
            request.session['Email']=Userdetails.Email
            return render(request,'index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid')
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'index.html')
    return render(request,'index.html')
