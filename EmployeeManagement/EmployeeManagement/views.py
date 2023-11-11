from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from database.models import empregister

def Home(request):
    return render(request,'home.html')

def NavBar(request):
    return render(request,'navbar.html')

def AddEmployee(request):
    return render(request,'add_employee.html')

def viewEmployee(request):
    return render(request,'view_employee.html')

def employeeRegister_form(request):
    if request.method == 'POST':
        id = request.POST.get('empoid')
        nam = request.POST.get('name')
        birt = request.POST.get('birth')
        emai = request.POST.get('email')
        pho = request.POST.get('phone')
        Add = request.POST.get('address')
        Jobb = request.POST.get('job')
        dep = request.POST.get('department')
       
        s1 =empregister(
            empoid=id,
            name=nam,
            birthdate=birt,
            email=emai,
            phone=pho,
            address=Add,
            jobtitle=Jobb,
            department=dep,
            
        )
        s1.save()
    return render(request,'add_employee.html') 

def view_datadisplay(request):
    s1 =empregister.objects.all()
    dict1 = {
        'data': s1
    }
    return render(request,'view_employee.html', dict1)

def dataDelete(request):
    e = request.GET['empoid']
    print("empoid=",e)
    s1=empregister.objects.get(empoid=e)
    s1.delete()
    return HttpResponseRedirect("/viewdisplay")

def DataChange(request):
    i1=request.GET['emid']
    n1=request.GET['na']
    b1=request.GET['br']
    e1=request.GET['em']
    p1=request.GET['ph']
    a1=request.GET['add'] 
    j1=request.GET['jo'] 
    d1=request.GET['de'] 

    dict1={
            'i1':i1,
            'n1':n1,
            'b1':b1,
            'e1':e1,
            'p1':p1,
            'a1':a1,
            'j1':j1,
            'd1':d1
            
           
    }
    return render(request,"employee_update.html",dict1)

def Dataupdate(request):
    empoid=request.GET['empoid']
    name=request.GET['name']
    birthdate=request.GET['birth']
    email=request.GET['email']
    phone=request.GET['phone']
    address=request.GET['address']
    jobtitle=request.GET['job']
    department=request.GET['department']
    s1=empregister.objects.get(empoid=empoid)
    s1.name=name
    s1.birthdate=birthdate
    s1.email=email
    s1.phone=phone
    s1.address=address
    s1.jobtitle=jobtitle
    s1.department=department
    s1.save()
    return HttpResponseRedirect("/viewdisplay")
