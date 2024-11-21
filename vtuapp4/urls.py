from django.urls import path
from vtuapp4 import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("login",views.Login,name="Login"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("logout",views.Logout,name="Logout"),
    path("fund",views.fund,name="fund"),
    path("formfund",views.formfund,name="formfund"),
    path("dataform",views.dataform,name="dataform"),
    path("buydata",views.buydata,name="buydata"),
    path("error",views.errorpage,name="errorpage"),
    path("buyairtime",views.buyairtime,name="buyairtime"),
    
]
