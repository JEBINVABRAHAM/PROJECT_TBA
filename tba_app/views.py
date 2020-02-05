from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from tba_app.models import registration,admin,contact
from datetime import date,timedelta,datetime
from django.contrib.auth import logout


# Create your views here.
#function for lawyer registration

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobileno=request.POST.get('mobileno')
        email=request.POST.get('email')
        types=request.POST.get('types')
        officeadd=request.POST.get('officeadd')
        residenceadd=request.POST.get('residenceadd')
        joiningdate=request.POST.get('joiningdate')
        duration=request.POST.get('duration')
        password=request.POST.get('password')

        a=registration(name=name, mobileno= mobileno,email=email,types=types,officeadd=officeadd,residenceadd=residenceadd,joiningdate=joiningdate,duration=duration,status='pending',password=password)
        a.save()
        return render(request,'index.html')
#function for viewing members
def regview(request):
    queryset=registration.objects.all()
    return render(request,'adminhome1.html',{'authors':queryset})

#function for approving registration
def approval(request):
    if request.method=='POST':
        id=request.POST.get('id')
        q=registration.objects.all().filter(id=id)[0]
        dur=q.duration
        join=q.joiningdate
        if dur=='3 Months':
            dd=90
        elif dur=='6 Months':
            dd=180
        elif dur=='1 Year':
            dd=365
        elif dur=='5 Year':
            dd=1825
        d=timedelta(dd)
        exp=join+d
        today = str(date.today())
        registration.objects.filter(id=id).update(status='approved',approvedate=today,expirydate=exp)
        return regview(request)

#function for login 
def authentication(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        email=str(email)
        password=str(password)
        u=admin.objects.filter(email=email,password=password)
        c=0
        if u.count()==1:
          
           return render(request,'adminhome.html') 
        else:
            u=registration.objects.filter(email=email,password=password,status='approved')
            if u.count()==1:
                request.session['email']=email
                qry=registration.objects.all().filter(email=email)
                return render(request,'lawyerhome.html')
            else:
                return HttpResponse('login unsuccesful')   

def lawyerdetails(request):
     queryset=registration.objects.all()
     return render(request,'member.html',{'authors':queryset})                


#function for logout
def logout_view(request):
    logout(request)
    return render(request,'index.html') 


#function to view lawyer profile
def viewlawprof(request):
     queryset=registration.objects.all().filter(email=request.session['email'])
     return render(request,'lawyerprofile.html',{'authors':queryset}) 

def  viewlawprofedit(request):
     queryset=registration.objects.all().filter(email=request.session['email'])
     return render(request,'lawyerprofedit.html',{'authors':queryset}) 

#function for editing lawyer profile
def lawyerdetailsedit(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobileno=request.POST.get('mobileno')
        email=request.POST.get('email')
        officeadd=request.POST.get('officeadd')
        residenceadd=request.POST.get('residenceadd')
        password=request.POST.get('password')
        registration.objects.filter(email=request.session['email']).update(mobileno=mobileno,officeadd=officeadd,residenceadd=residenceadd,password=password)
    return render(request,'lawyerhome.html')


#function for adding message
def submitmsg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        b=contact(name=name,emailid=email,subject=subject,msg=message,status='off')
        b.save()
        return render(request,'index.html')

def viewmsg(request):
    queryset=contact.objects.all().filter(status='off')
    return render(request,'adminmsg.html',{'authors':queryset})

def readmsg(request):
    if request.method=='POST':
        id=request.POST.get('id')
        contact.objects.filter(id=id).update(status='on')
        return viewmsg(request)


