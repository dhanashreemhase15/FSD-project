from django.shortcuts import render,HttpResponse,redirect
from fsd_app.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    context={}
    context['x']=100
    context['y']=150
    context['mylist']=[10,20,30,40,50]
    #return HttpResponse("In home functions")
    return render(request,'home.html',context)

def create(request):
    if request.method=='POST':  #GET==POST
        n=request.POST['sname']
        e=request.POST['semail']
        m=request.POST['mob']
        a=request.POST['adr']
        s1=Student.objects.create(name=n,email=e,mobile=m,address=a)
        s1.save()
        return HttpResponse("Data is stored")
    else:
        return render(request,'create.html')

def dashboard(request):
    s1=Student.objects.all()    #2 records
    #print(s1)
    context={}
    context['data']=s1
    return render(request,'dashboard.html',context)


def delete(request,rid):  #rid=2
    s1=Student.objects.filter(id=rid)
    s1.delete()
    return redirect('/dashboard')

def edit(request,rid):
    if request.method=='POST':
        un=request.POST['sname']
        ue=request.POST['semail']
        um=request.POST['mob']
        ua=request.POST['adr']
        s1=Student.objects.filter(id=rid)
        s1.update(name=un,email=ue,mobile=um,address=ua)
        return redirect('/dashboard')
    else:
        #display form with old data
        s1=Student.objects.get(id=rid)    #Student object (1)
        # print(s1)
        context={}
        context['data']=s1
        return render(request,'edit.html',context)
    
#----------------------------------------------
def index(request):
    # userid=request.user.id
    # print(userid)
    # print(request.user.is_authenticated)
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        context={}
        if uname=="" or upass=="" or ucpass=="":# T
            context['errmsg']="Fields can not be empty"
        elif upass != ucpass:
            context['errmsg']="Password and confirm password are not same"
        else:
            try:
                u=User.objects.create(password=upass,username=uname,email=uname)
                u.set_password(upass)
                u.save()
                context['success']="User created successfully, Please login"
            except Exception:
                context['errmsg']="User already exist !!!!"
        return render(request,'register.html',context)
    else:
        return render(request,'register.html')
    

def user_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=="" or upass=="":# T
            context['errmsg']="Fields can not be empty"
        else:
            u=authenticate(username=uname,password=upass)
            # print(u)
            if u is not None:
                login(request,u)
                return redirect('/')
        return render(request,'login.html',context)

    else:
        return render(request,'login.html')
    

def user_logout(request):
    logout(request)
    return redirect('/')