
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone







class users (AbstractUser):
    balance=models.FloatField(default=0.00,blank=True,verbose_name="balance" )
    purchase_total=models.FloatField(default=0.00,blank=True, )
    


    #def __str__ (self):
       
       #return self.balance
   
class historie (models.Model):
    number=models.CharField(max_length=200)
    history=models.CharField(default="no trasaction yet", max_length=100)
    userss = models.ForeignKey(users,on_delete=models.CASCADE, null=True, verbose_name = "use")
    dates=models.DateTimeField(auto_now_add=True,)
    def __str__(self) -> str:
       return f"{self.userss} history"
    

   
    class Meta:
     verbose_name_plural = "history"


historie.objects.order_by("dates")

class purchase (models.Model):
    number=models.CharField(max_length=200)
    userss = models.ForeignKey(users,on_delete=models.CASCADE, null=True, verbose_name = "use")
    dates=models.DateTimeField(auto_now_add=True,)
    def __str__(self) -> str:
       return f"{self.userss} purchase"
    



   

   


    
 
   
    


    



# Create your models here.
