from django.http import HttpResponse,HttpResponseRedirect 
from django.shortcuts import render
from service.models import Employee

def homePage(request):
    # return HttpResponse("I am from home page")
    return render(request,'index.html')

def aboutPage(request):
    # return HttpResponse("I am from about page")
     return render(request,'about.html')

def contactPage(request):
    return render(request,'contact.html')

def helpPage(request):
    return render(request,'help.html')

def addUser(request):
    msg=''
    if request.method=="POST":
        name=request.POST['full_name']
        email=request.POST['email_id']
        mobile_num=request.POST['mobile_num']
        password=request.POST['pass']
        data=Employee(full_name=name,email_id=email,mob_num=mobile_num,password=password)
        data.save()
        msg="Record Inserted Succesfully !"
        # print(name+" "+email_id+" "+mobile_num+" "+password)
    return render(request,'adduser.html',{"message":msg})

def userList(request):
    data=Employee.objects.all().values()
    # print(data)
    return render(request,'userlist.html',{'mydata':data})

def deleteuser(request,id):
    msg=''
    data = Employee.objects.get(id=id)
    # print(data)
    data.delete()
    msg="Record Deleted Sucessfully !"
    # return render(request,'userlist.html',{"message":msg})
    return HttpResponseRedirect('/user-list')

def editUser(request,id):
    data1 = Employee.objects.get(id=id)
    # print(data1)
    context = {
        'mydata': data1,
    }
    return render(request,'update.html',context)

def updateUser(request,id):
    name=request.POST['full_name']
    email_id=request.POST['email_id']
    mob_num=request.POST['mobile_num']
    password=request.POST['pass']
    # print(name+" "+email_id+" "+mob_num+" "+password)
    member = Employee.objects.get(id=id)
    member.full_name=name
    member.email_id=email_id
    member.mob_num=mob_num
    member.password=password
    member.save()
    msg='Updated message succesfully !'
    return HttpResponseRedirect('/user-list')
    
    

