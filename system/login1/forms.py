from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Contact, Productdb,ITCategory,Subcategory
class EmployeeRegistation(forms.ModelForm):
    class Meta:
     model = User
     fields = ['id','first_name','last_name','username','email','password','is_superuser']
     help_texts = {
            'username': None,
            'is_superuser': None,
        }
     widgets = {
         'first_name':forms.TextInput(attrs={'style': 'width:220px'}),
         'last_name':forms.TextInput(attrs={'style': 'width:220px'}),
         'username':forms.TextInput(attrs={'style': 'width:220px'}),
         'email':forms.TextInput(attrs={'style': 'width:220px'}),
         'password':forms.PasswordInput(attrs={'style': 'width:220px'}),
         
     }
     labels = {'is_superuser':'Admin permissions','email':'Email_ ID  '}

    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            raise ValidationError("first name is required.")
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if self.cleaned_data["last_name"].strip() == '':
            raise ValidationError("Last name is required.")
        return self.cleaned_data["last_name"]

    def clean_email(self):
        email = self.cleaned_data['email']
        validator = RegexValidator("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
        validator(email)
        return email

class LoginForm(forms.ModelForm):
    class Meta:
     model = User
     fields = ['username','password']
     widgets = {
        
         'username':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
         'password':forms.PasswordInput(attrs={'class':'form-control form-control-sm'})
        ,
     }

class UserProfileChange(forms.ModelForm):
    class Meta:
     model = User
     fields = ['first_name','last_name','username','email']
     labels = {'email':'Email ID'}

class UpdateForm(forms.ModelForm):
    class Meta:
     model = User
     fields = ['id','first_name','last_name','username','email']
     labels = {'email':'Email ID'}

class ProductRegistation(forms.ModelForm):
    class Meta:
        model = Productdb
        fields =[ 'pid','category','subcategory','product_name','product_brand','serial_no','model_no','description']
        widgets = {
        'pid':forms.TextInput(attrs={'class':'form-control form-control-user'}),
        'category':forms.Select(attrs={'class':'form-control form-control-user'}) ,
        'subcategory':forms.Select(attrs={'class':'form-control form-control-user'}) ,
        'product_name':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
        'product_brand':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
        'serial_no':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
        'model_no':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
        'description':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
         }
        labels = {'product_id':'Product ID'}
   

class AddCategory(forms.ModelForm):
    class Meta:
        model = ITCategory
        fields =['category']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields =['subcategory','category']
        widgets ={
             'category':forms.Select(attrs={'class':'form-control form-control-user'}) ,
             'subcategory':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['name','email','message']
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
        'email':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
        'message':forms.Textarea(attrs={'class':'form-control form-control-user'}) ,
        
         }
       