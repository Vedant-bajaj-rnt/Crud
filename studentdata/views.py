from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Studentdata.models import Studentdata
import mysql.connector as connecter


# Create your views here.
def Home(request):
    data = Studentdata.objects.all()
    return render(request,"Home.html",{'data':data})

def send(request):
    if request.method=="POST":
        Name = request.POST["Name"]
        Surname = request.POST["Surname"]
        Studentdata(NAME=Name,SURNAME=Surname).save()
        data = Studentdata.objects.all()
        return render(request,"Home.html",{'data':data})

def delete(request):
    if request.method=="POST":
        ID = request.POST['id']
        Studentdata.objects.filter(ID=ID).delete()
        data = Studentdata.objects.all()
        return HttpResponseRedirect("Home",{'data':data})

def edit(request):
    if request.method=="POST":
        Id = request.POST["id"]
        Name = request.POST["Name"]
        Surname = request.POST["Surname"]
        Studentdata.objects.filter(ID=Id).update(NAME=Name,SURNAME=Surname)
        data = Studentdata.objects.all()
        return render(request,"Home.html",{'data':data})
