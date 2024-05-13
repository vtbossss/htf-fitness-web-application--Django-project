from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from auth_app.models import Contact,Bmi
from math import pi



# Create your views here.


def home(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        contactus=Contact(name=name,email=email,subject=subject,message=message)
        contactus.save()
        messages.success(request,"we will get back to you soon")
        return redirect('/#contact')

    return render(request,"index.html")


def signup(request):

    if(request.method=="POST"):
        phone=request.POST.get("usernumber")
        email=request.POST.get("email")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")


        
        
        if(pass1!=pass2):
            messages.info(request,"password did not match")
            return redirect('/signup')
        
        
        try:
            if(User.objects.get(phone=phone)):
                messages.warning(request,"Phone number is already taken")
                return redirect('/signup')
        except Exception as identifier:
            pass

        try:
            if(User.objects.get(email=email)):
                messages.warning(request,"email is already taken")
                return redirect('/signup')
        except Exception as identifier:
            pass

        newuser=User.objects.create_user(phone,email,pass1,last_name=lname,first_name=fname)
        newuser.save()
        messages.success(request,"user is added")
        return redirect('/login')
    return render(request,"signup.html")


        



def dologin(request):
    if not request.user.is_authenticated:
        messages.info(request,"Please Login to Continue")
    if(request.method=="POST"):
        phone=request.POST.get("usernumber")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=phone,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect("/")
        else:
            messages.error(request,"Wrong Credentials")
            return redirect("/login")

    return render(request,'login.html')
def dologout(request):
    logout(request)
    messages.success(request,"Logout successful")
    return redirect("/login")

def bcalc(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('/login')
    if(request.method=='POST'):

        weight_metric=request.POST.get('weight-metric')
        weight_imperial=request.POST.get('weight-imperial')
        if weight_metric:
            weight=float(request.POST.get('weight-metric'))
            height=float(request.POST.get('height-metric'))
        elif weight_imperial:
            weight=round(float(request.POST.get('weight-imperial'))/2.205)
            height=round((float(request.POST.get('feet'))*30.48+float(request.POST.get("inches"))*2.54)/100)
        bmi=(weight/(height**2))
        ssave=request.POST.get('save')
        if(ssave=='on'):
            Bmi.objects.create(user=request.user,weight=weight,height=height,bmi=round(bmi))
        if bmi < 16:
            state = "Severe Thinness"
        elif bmi > 16 and bmi < 17:
            state = "Moderate Thinness"
        elif bmi > 17 and bmi < 18:
            state = "Mild Thinness"
        elif bmi > 18 and bmi < 25:
            state = "Normal"
        elif bmi > 25 and bmi < 30:
            state = "Overweight"
        elif bmi > 30 and bmi < 35:
            state = "Obese Class I"
        elif bmi > 35 and bmi < 40:
            state = "Obese Class II"
        elif bmi > 40:
            state = "Obese Class III"

        context["bmi"] = round(bmi)
        context["state"] = state
    
            
    return render(request,'bmi.html',context)
def ccalc(request):

    context={}
    if not request.user.is_authenticated:
        return redirect('/login')
    if(request.method=="POST"):
        
        weight=float(request.POST.get('weight'))
        height=float(request.POST.get('height'))
        age=int(request.POST.get('age1'))
        gender=bool(request.POST.get('gender'))
        activity=int(request.POST.get('activitylevel'))
        if(gender):
            bmr=round(10 * weight + 6.25 * height - 5 * age + 5)
        else:
            bmr=round(10 * weight + 6.25 * height - 5 * age - 161)
        if(activity==1):
            calorie=round(bmr*1.2)
        elif(activity==2):
            calorie=round(bmr*1.375)
        elif(activity==3):
            calorie=round(bmr*1.55)
        elif(activity==4):
            calorie=round(bmr*1.725)
        else:
            calorie=round(bmr*1.9)
        context['cal']=calorie
        context['bulk']=calorie+250
        context['cut']=calorie-250
        
            
    return render(request,'calorie.html',context)
def mcalc(request):
    context={}
    if not request.user.is_authenticated:
        return redirect('/login')
    if(request.method=="POST"):
        
        weight=float(request.POST.get('weight'))
        height=float(request.POST.get('height'))
        age=int(request.POST.get('age1'))
        gender=bool(request.POST.get('gender'))
        activity=int(request.POST.get('activitylevel'))
        if(gender):
            bmr=round(10 * weight + 6.25 * height - 5 * age + 5)
        else:
            bmr=round(10 * weight + 6.25 * height - 5 * age - 161)
        if(activity==1):
            calorie=round(bmr*1.2)
        elif(activity==2):
            calorie=round(bmr*1.375)
        elif(activity==3):
            calorie=round(bmr*1.55)
        elif(activity==4):
            calorie=round(bmr*1.725)
        else:
            calorie=round(bmr*1.9)
        protein=(0.25*calorie)/4
        carb=(0.5*calorie)/4
        fat=(0.25*calorie)/9
        context['p']=round(protein)
        context['c']=round(carb)
        context['f']=round(fat)


        
            
    return render(request,'macro.html',context)
def work(request):
    return render(request,'workout.html')

def nutrition(request):
    return render(request,'nutrition.html')
def profile(request):
    u=request.user
    post=User.objects.filter(username=u)
    context={'post':post}
    return render(request,'profile.html',context)







