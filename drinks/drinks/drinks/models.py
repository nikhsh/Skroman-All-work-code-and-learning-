from pyexpat import model
from django.db import models


class Drink(models.Model):
    F_Name = models.CharField(max_length=200,null=False)
    L_Name = models.CharField(max_length=200,null=False)
    E_Mail = models.EmailField(max_length=254,null=False)
    Password = models.CharField(max_length=100,null=False)
    Create_Password = models.CharField(max_length=100,null=False)
    Mobile_No = models.CharField(max_length=100, null=False)
    Art_Type = models.CharField(max_length=100, null=False)


    def __str__(self):
        return "{} - {}".format(self.F_Name,self.L_Name,self.E_Mail,self.Password,self.Create_Password,self.Mobile_No,self.Art_Type)
        
