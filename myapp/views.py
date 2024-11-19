from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def service(request):
    return render(request,'service-details.html')
def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def doctor(request):
    return render(request,'doctor.html')
def myservice(request):
    return render(request,'services.html')

def appointment(request):
    if request.method == "POST":
        myappointments=Appointment1(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor = request.POST['doctor'],
            message=request.POST['message'],

        )
        myappointments.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment.html')

    #return render(request,'appointment.html')


def show(request):
    allappointments=Appointment1.objects.all()
    return render(request,'show.html',{'appointment':allappointments})




def delete(request,id):
    appoint=Appointment1.objects.get(id=id)
    appoint.delete()
    return redirect('/show')



def contact(request):
    if request.method == "POST":
        savedinfor=Contact1(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        savedinfor.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

def edit(request,id):
    editappoint=Appointment1.objects.get(id=id)
    return render(request, 'edit.html',{'appointment':editappoint})
