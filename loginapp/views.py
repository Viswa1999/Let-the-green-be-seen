#from django.http import request
from django.shortcuts import redirect, render
from .models import User
import mysql.connector 
from django.contrib import messages
from operator import itemgetter
#from . models import Image
#from .form import ImageForm
#from django.contrib.auth.models import  auth
# Create your views here.
def welcome(req):
    return render(req,'welcome.html')
def login(req):
    con=mysql.connector.connect(host="localhost",user="root",password="Prasad@07",database="project")
    cursor=con.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",password="Prasad@07",database="project")
    cursor2=con2.cursor()
    sqlcommand="select email from loginapp_user"
    sqlcommand2="select password from loginapp_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    
    res=list(map(itemgetter(0),e))
    res2=list(map(itemgetter(0),p))
    print(res)
    print(res2)

    if req.method=="POST":
        email=req.POST['email']
        password=req.POST['password']

        """user = auth.authentication(email = email, password = password)
        if user is not None:
            auth.login(req,user)
            return redirect("/")
        else:
            messages.info(req,'invalid credentials')
            return redirect('login')"""
        i=1
        k=len(res)
        while i<k:
            if res[i] == email and res2[i] == password:
                return render(req,'welcome.html',{'email':email})
                
                break
            i+=1
        else:
            messages.info(req,"Check email or password")
            return redirect('login')
    return render(req,'login.html')
def register(req):
    if req.method=="POST":
        #user = User()
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        email=req.POST.get('email')
        password=req.POST.get('password')
        repassword=req.POST.get('repassword')
        if User.objects.filter(email=email).exists():
            messages.warning(req,'email is already exists')
            return redirect('register')
        
        else:
            if password!=repassword:
                messages.info(req,'passwords are not same')
                return redirect('register')
            elif fname=="" or password=="":
                messages.info(req,'fields are empty')
                return redirect('register')
            else:
                User.save()
                return redirect('welcome')
    return render(req,'register.html')
def payment(req):
    return render(req,'payment.html')

"""def index(req):
    if req.method == "POST":
        form = ImageForm(data=req.POST,files=req.FILES) # important files for uploading images
        if form.is_valid():
            form.save()
            obj = form.instance # to see what the user have uploaded
            return render(req,"index.html",{"obj":obj})
    else:
        form = ImageForm()
    img = Image.objects.all()

    return render(req,"index.html",{"img":img,"form":form})"""