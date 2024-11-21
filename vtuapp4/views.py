
from django.shortcuts import render,redirect
from vtuapp4.models import users,historie,purchase
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import requests
from django.utils import timezone


# HOME PAGE
def home (request):
    return render(request,"frontview/frontview.html")

# REGISTER PAGE

def register (request):
     if request.method=="POST":
     
      username=request.POST.get("username")
      email=request.POST.get("email")
      first_name=request.POST.get("firstname")
      last_name=request.POST.get("lastname")
      password=request.POST.get("password")
      user=users.objects.create_user(username=username,email=email,password=password)
      user.first_name=first_name
      user.last_name=last_name
      user.save()
      return redirect(Login)
     return render(request,"register.html")

    


    
# LOGIN PAGE

def Login (request):
    if request.method=="POST":

     usernamee=request.POST.get("username")
     passwordd=request.POST.get("password")
     user=authenticate(username=usernamee,password=passwordd)
     login(request,user)
     return redirect(dashboard)
    

    return render(request,"login.html")



# DASHBOARD PAGE

def dashboard (request):

    if request.user.is_authenticated :
       usersss=request.user
       
       historyy=historie.objects.filter(userss=request.user )
       purchas=purchase.objects.filter(userss=request.user )
       
       usersss= {"user":usersss,
        "users":historyy,
        "userss":purchas
        }
       
    return render(request,"dashboard.html",usersss )


 # LOGOUT CODE
def Logout (request):
    logout(request)
    
    return redirect(Login)
    



def formfund (request):
    user=request.user.username
    return render(request,"formfund.html",{"user":user})


def fund (request):
    if request.method=="GET":
     amount=request.GET.get("amount")
     bal=request.user.balance
     if amount != 0 :
       result=float(bal)+float(amount)

       update=users.objects.update(balance=result)
       user=historie.objects.create(userss=request.user,history=F"you have added {amount} to your wallet and it  was successful......\n. ")
       
       

       

       return redirect(dashboard)
       
    return render(request,"fund.html", )


def dataform (request):
    return render(request,"dataform.html")



def buydata (request):
    if request.method=="GET":
     mobilenumber=request.GET.get("mobilenumber")
     dataplan=request.GET.get("dataplan")
     mobilenetwork=request.GET.get("mobilenetwork")
     user=request.user.balance
     usser=request.user.purchase_total
    

     url="https://www.nellobytesystems.com/APIDatabundleV1.asp?"

     api=f"{url}&MobileNetwork={mobilenetwork}&DataPlan={dataplan}&MobileNumber={mobilenumber}RequestID=request_id&CallBackURL=callback_url"

     if float(user)>=int(dataplan)  :
    #    response=requests.get(api).json()
       



       userss=float(user)-float(dataplan)
       purchasee=float(usser)+float(dataplan)

       usersss=users.objects.update(balance=userss)
       purchaseee=users.objects.update(purchase_total=purchasee)
       
       if mobilenetwork=="01":
          mobilenetwork="MTN"
          user=purchase.objects.create(userss=request.user,number=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful...... ")
          user=historie.objects.create(userss=request.user,history=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful...... ")
          
          return redirect(dashboard)
       
       if mobilenetwork=="02":
          mobilenetwork="Glo"
          user=purchase.objects.create(userss=request.user,number=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful......\n. ")
          user=historie.objects.create(userss=request.user,history=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful...... ")
          return redirect(dashboard) 
       if mobilenetwork=="03":
          mobilenetwork="9mobile"
          user=purchase.objects.create(userss=request.user,number=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful......\n. ")
          user=historie.objects.create(userss=request.user,history=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful...... ")
          return redirect(dashboard)
          
       if mobilenetwork=="04":
          mobilenetwork="Airtel"
          user=purchase.objects.create(userss=request.user,number=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful......\n. ")
          user=historie.objects.create(userss=request.user,history=F"you have purchase {dataplan}MB of {mobilenetwork} to this {mobilenumber} and it  was successful...... ")
          

          return redirect(dashboard)
    
       else:
              return redirect(errorpage)

    return render(request,"buydata.html")

def errorpage (request):
    return render(request,"error_page.html")


def buyairtime (request):
    return render(request,"buyairtime.html")




# Create your views here.
