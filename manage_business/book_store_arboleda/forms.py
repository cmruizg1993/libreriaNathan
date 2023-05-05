from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class Createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email','password1', 'password2'] 

 
class Createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
 
class Createbookform(ModelForm):
    class Meta:
        model=Book
        fields='__all__'