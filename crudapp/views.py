from django.shortcuts import render
from django.http import HttpResponse
from crudapp.models import Student

# Create your views here.
def crud_opertions(request):
    if request.method=="GET":
        b=request.GET['b']
        if b=="Add":
            resp=insert_data(request)
            return resp
        elif b=="Update":
            resp=update_data(request)
            return resp
        elif b=="Delete":
            res=delete_data(request)
            return res
        elif b=="Result":
            res=result(request)
            return res

def insert_data(request):
    rno=request.GET.get("rno")
    s1=request.GET.get("sub1")
    s2=request.GET.get("sub2")
    stud=Student(rollno=rno,subject1=s1,subject2=s2)
    stud.save()

    msg={'msg':"Marks are Added"}
    r=render(request,"home.html",context=msg)
    return r

def update_data(request):
    rno=request.GET.get("rno")
    stud=Student.objects.get(rollno=rno)
    stud.rollno=rno
    stud.subject1=request.GET.get("sub1")
    stud.subject2=request.GET.get("sub2")
    stud.save()
    msg={'msg':"Marks updated"}
    r=render(request,"home.html",context=msg)
    return r

def delete_data(request):
    rno=request.GET.get("rno")
    stud=Student.objects.get(rollno=rno)
    stud.delete()
    msg={'msg':"Marks Deleted"}
    r=render(request,"home.html",context=msg)
    return r

def result(request):
    rno=request.GET.get("rno")
    stud=Student.objects.get(rollno=rno)
    output=f'''<h2> Rollno {rno}<br>
             Subject1 {stud.subject1}<br>
             Subject2 {stud.subject2}<br>'''
    res="pass" if stud.subject1>=40 and stud.subject2>=40 else "fail"
    output=output+"Result "+res
    return HttpResponse(output)

def home(request):
    r=render(request,"home.html")
    return r
        
        