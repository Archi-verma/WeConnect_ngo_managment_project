from tkinter import messagebox
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import *
import mysql.connector as sql

# Create your views here.
def home(request):
    if (request.method=="POST"):#for user details
        
        data=request.POST
        username=data.get('username')
        email=data.get('email')
        phone=data.get('phone')
        address=data.get('address')
        city=data.get('city')
        area=data.get('area')
        userinfo.objects.create(
        username=username,
        email=email,
        phone=phone,
        address=address,
        city=city,
        area=area
        )
        return redirect(userlogin)
    return render(request,"home/main.html")
def form(request):
    return render(request,"home/ngoform.html")
def userlogin(request):
    if(request.method=="POST"):
        m=sql.connect(host="localhost",user="root",passwd="2606",database="django")
        cursor=m.cursor()
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        print(username,phone)
        c="select * from home_userinfo where username='{}' and phone={} ".format(username,phone)
        cursor.execute(c)
        t=cursor.fetchall()
        print(t)
        print("all record")
        if not t:
             return render(request,"home/error.html",{'error': 'No matching user found'})
        else:
             a="select * from home_campaign"
             cursor.execute(a)
             b=cursor.fetchall()
             print(b)
             return render(request,"home/usermain.html",{'username':username,'b':b})
    return render(request,"home/userlogin.html",)

def ngologin(request):
    if(request.method=="POST"):
        m=sql.connect(host="localhost",user="root",passwd="2606",database="django")
        cursor=m.cursor(dictionary=True)
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        c="select * from home_ngo_info where email='{}' and password={} ".format(email,password)
        cursor.execute(c)
        t=cursor.fetchone()
        print(t)
        id=t['ngoid']
        print("id of user is",id)
        if not t:
             return render(request,"home/error.html",{'error': 'No matching user found'})
        else:
            url="/ngomain/?output={}".format(id)
            return HttpResponseRedirect (url)

    return render(request,"home/ngologin.html")

def error(request):
    return render(request,"home/error.html")

def payment(request):
    return render(request,"home/payment.html")

def donor(request):
    return render(request,"home/donor.html")


def usermain(request):
    test=""
    try:
        m=sql.connect(host="localhost",user="root",passwd="2606",database="django")
        cursor=m.cursor()
        cursor.execute("select * from home_campaign")
        data=cursor.fetchall()
        print(data)
        test=data
    except:
        test="failure in conneting database"


    return render(request,"home/usermain.html",{'test':test})

def ngomain(request):
      output=request.GET.get('output')
      m=sql.connect(host="localhost",user="root",passwd="2606",database="django")
      cursor=m.cursor(dictionary=True)
      a="select * from home_campaign where ngoid={}".format(output)        
      cursor.execute(a)
      b=cursor.fetchall()
      cursor.close()
      print(b)
      if (request.method=="POST"):
           m=sql.connect(host="localhost",user="root",passwd="2606",database="django")
           cursor=m.cursor(dictionary=True)
           name = request.POST.get('campaign-name')
           description = request.POST.get('description')
           cemail = request.POST.get('contact-email')
           cname = request.POST.get('contact-name')
           cphone = request.POST.get('contact-phone')
           edate = request.POST.get('end-date')
           goalamount = request.POST.get('goal-amount')
           sdate = request.POST.get('start-date')
           ngoid = request.POST.get('ngoid')
           campaing_id = request.POST.get('random-id')
        
           print(name, ngoid, sdate)  # For debugging purposes
        
        # Create the SQL query with placeholders
           query = """
            INSERT INTO home_campaign 
            (name, description, cemail, cname, cphone, edate, goalamount, sdate, ngoid, campaing_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    # Execute the query with the provided values
           cursor.execute(query, (name, description, cemail, cname, cphone, edate, goalamount, sdate, ngoid, campaing_id))        
           m.commit()
           cursor.close()
           m.close()
           messages.success(request,'Form is submitted')
        
      return render(request, "home/ngomain.html",{'output':output,'b':b})

def register(request):
    if (request.method=="POST"):# for ngo details
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        phone=data.get('phone')
        address=data.get('address')
        password=data.get('password')
        confirm_password=data.get('confirm_password')
        mission=data.get('mission')
        area=data.get('area')
        NGO_info.objects.create(
        name=name,
        email=email,
        phone=phone,
        address=address,
        password=password,
        confirm_password=confirm_password,
        mission=mission,
        area=area
        )
        return HttpResponseRedirect("/ngologin/")
    return render(request,"home/ngo_registration.html")