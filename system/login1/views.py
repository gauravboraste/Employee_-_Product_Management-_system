
from django.contrib.auth.models import User
from django.forms.widgets import Select
from django.http import response
from xlwt.Worksheet import Worksheet
from login1.models import  Contact, Employee, ITCategory, Productdb, Subcategory
from login1.forms import AddCategory, ContactForm, EmployeeRegistation, LoginForm, ProductRegistation,UserProfileChange,UpdateForm,SubCategoryForm
from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import  redirect, render
from django.contrib.auth  import authenticate,  login,logout
from django.urls import reverse

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q
import xlwt 
import datetime
from openpyxl import Workbook
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'index.html')



def registers(request):
    if request.method == 'POST':
        fm = EmployeeRegistation(request.POST)
        if fm.is_valid():
            fn=fm.cleaned_data['first_name']
            ln=fm.cleaned_data['last_name']
            un=fm.cleaned_data['username']
            em=fm.cleaned_data['email']
            pw=make_password(fm.cleaned_data['password'])
            su=fm.cleaned_data['is_superuser']
            #dp=fm.cleaned_data['department']
           
            reg =User(first_name=fn,last_name=ln,username=un,email=em,password=pw,is_superuser=su)
            #User.pw=make_password(User.password)
            
            reg.save()
            messages.success(request, "Registation successfully!")
            return render(request,'index.html')
        else:
             messages.success(request, "Enter vaild details Registation Unsuccessfully!!!")
             return render(request,'registers.html',{'form':fm})
    else:
        fm=EmployeeRegistation()
        return render(request,'registers.html',{'form':fm})
       
def loginin(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        ad = authenticate(request,username=username,password=password)
        
        if ad is not None and ad.is_superuser:
            login(request, ad)
            messages.success(request, "Login successfully !!!")
            return HttpResponseRedirect('/adminprofile/')
            
        if ad:
                login(request,ad)
                messages.success(request, "Login successfully!")
                return HttpResponseRedirect('/profile/')


        else:
            messages.success(request, "Login Unsuccessfully! Check Enter Details")
            return render(request,'login.html')
    else:
        return render(request,"login.html")

def profile(request):
    if request.user.is_authenticated:
         if request.method =="POST":
             fm =UserProfileChange(request.POST,instance=request.user)
             if fm.is_valid():
                fm.save()
         else:
            fm = UserProfileChange(instance=request.user)
            return render(request,'profile.html',{'name':request.user, 'form':fm})
    else:
        return render(request,'profile.html')

def adminprofile(request):
    if request.user.is_authenticated:
         if request.method =="POST":
             fm =UserProfileChange(request.POST,instance=request.user)
             if fm.is_valid():
                fm.save()
         else:
            fm = UserProfileChange(instance=request.user)
            return render(request,'adminprofile.html',{'name':request.user, 'form':fm})
    else:
        return render(request,'adminprofile.html')

def logoutuser(request):
    
        logout(request)
        messages.success(request, "Logout  successfully  !")
        return redirect('login')
@login_required(login_url='/login/')
def emp_showdata(request):
    data = Employee.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        show=User.objects.filter(Q(first_name__icontains=q)|Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(username__icontains=q)|Q(email__icontains=q)|Q(is_superuser__icontains=q))
        return render(request,'emp_showdata',{'dat':show})
    
    else: 
     data = User.objects.all()
     return render(request,'emp_showdata.html',{'dat':data})


def delete_items(request, pk):
	queryset = User.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
        
		return redirect('/showdata')
	return render(request, 'delete_items.html',{'data':queryset})




def update_data(request,id):
    if request.method == "POST":
        pi =User.objects.get(pk=id)
        fm =EmployeeRegistation(request.POST or None,instance=pi)
        if fm.is_valid():
            fm.save()
        messages.success(request,"Update Data Successfully !!!!")
        return redirect('showdata')
    else:
        pi =User.objects.get(pk=id)
        return render(request, 'updateemp.html',{'form':pi})


def catshow(request):
    cat = ITCategory.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        show=ITCategory.objects.filter(Q(category__icontains=q))
        return render(request,'catshow.html',{'dat':show})
        
    else: 
     cat = ITCategory.objects.all()
     return render(request,'catshow.html',{'dat':cat})















def emp_export_excel(request):
    myuser1 = User.objects.all()
    response =HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=report'+\
       str(datetime.datetime.now())+'.xls'
       
    wb = xlwt.Workbook(encoding='utf-8')
    ws =wb.add_sheet('User')
    row_num = 0
    font_style =xlwt.XFStyle()
    font_style.font.bold = True
    
    columns =['id','first_name','last_name','username','email']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('id','first_name','last_name','username','email')
    

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    messages.success(request," Excel Downloaded !!!!")
    wb.save(response)
    return response
    


def product_register(request):
     if request.method == 'POST':
        fm = ProductRegistation(request.POST)
        if fm.is_valid():
            pd=fm.cleaned_data['pid']
            ct=fm.cleaned_data['category']
            sct=fm.cleaned_data['subcategory']
            pn=fm.cleaned_data['product_name']
            pb=fm.cleaned_data['product_brand']
            sn=fm.cleaned_data['serial_no']
            mn=fm.cleaned_data['model_no']
            ds=fm.cleaned_data['description']


           
           
            reg =Productdb(pid=pd,category=ct,subcategory=sct,product_name=pn,product_brand=pb,serial_no=sn,model_no=mn,description=ds)
            # #User.pw=make_password(User.password)
            reg.save()
            messages.success(request, "Registation successfully!")
            return render(request,'index.html')
        else:
             messages.success(request, "Enter vaild details Registation Unsuccessfully!!!")
             return render(request,'product_register.html',{'form':fm})
     else:
        fm=ProductRegistation()
        return render(request,'product_register.html',{'form':fm})


@login_required(login_url='/login/')
def productshow(request):
    data = Productdb.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
       
        show=Productdb.objects.filter(Q(id__icontains=q)|Q(pid__icontains=q)|Q(product_name__icontains=q)|Q(product_brand__icontains=q)|Q(serial_no=q)|Q(model_no__icontains=q)|Q(description__icontains=q)|Q(category__icontains=q)|Q(subcategory__icontains=q))
    
        return render(request,'productdatashow.html',{'dat':show})
    
    else: 
     data = Productdb.objects.all()
     return render(request,'productshow.html',{'dat':data})


def cat_product(request):
     if request.method == 'POST':
        fm = AddCategory(request.POST)
        if fm.is_valid():
            
            ct=fm.cleaned_data['category']

            reg =ITCategory(category=ct)
            # #User.pw=make_password(User.password)
            reg.save()
            messages.success(request, "Category Added successfully!")
            return render(request,'index.html')
        else:
             messages.success(request, "Enter vaild details Registation Unsuccessfully!!!")
             return render(request,'cat_product.html',{'form':fm})
     else:
        fm=AddCategory()
        return render(request,'cat_product.html',{'form':fm})

def cattable(request):
    cat = ITCategory.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        show=ITCategory.objects.filter(Q(category__icontains=q))
        return render(request,'catproduct.html',{'dat':show})
        
    else: 
     cat = ITCategory.objects.all()
     return render(request,'catproduct.html',{'dat':cat})
    
import csv
def pro_export(request):
    
    rows = Productdb.objects.all()
    response =HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Product_report'+\
       str(datetime.datetime.now())+'.xls'
       
    wb = xlwt.Workbook(encoding='utf-8')
    ws =wb.add_sheet('User')
    row_num = 0
    font_style =xlwt.XFStyle()
    font_style.font.bold = True
    
    columns =['PID','Product Name','Product Brand','Serial No','Model No','Description','Category','SubCategory']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()

    
    

    for row in rows:
        row_num += 1

        row = [
            row.pid,
            row.product_name,
            row.product_brand,
            row.serial_no,
            row.model_no,
            row.description,
            row.category,
            row.subcategory,
        ]

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    
    wb.save(response)
    return response
    
    




def productdelete(request,id):
    det = Productdb.objects.get(id=id)

    if request.method == 'POST':
	    det.delete()
            
	    return redirect('/productshow')
    messages.success(request,"Delete Successfully !!!")
    return render(request, 'productdelete.html',{'delete':det})


def productupdate(request,id):
    if request.method == "POST":
        pi =Productdb.objects.get(pk=id)
        fm =ProductRegistation(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        messages.success(request,"Product Update Data Successfully !!!!")
        return redirect('productdatashow')
    else:
        pi =Productdb.objects.get(pk=id)
        fm =ProductRegistation(instance=pi)
        return render(request, 'productupdate.html',{'form':fm})


def catdelete(request,id):
     det = ITCategory.objects.get(id=id)

     if request.method == 'POST':
	     det.delete()
        
	     return redirect('/catshow')
     return render (request, 'cat_delete.html',{'delete':det})


def addsubcategory(request):
    if request.method == 'POST':
        fm = SubCategoryForm(request.POST)
        if fm.is_valid():
            
            sct=fm.cleaned_data['subcategory']
            ct=fm.cleaned_data['category']
            
            reg =Subcategory(subcategory=sct,category=ct)
            reg.save()
            messages.success(request, "SubCategory Added successfully!")
            return render(request,'index.html')
        else:
             messages.success(request, "Enter vaild details Registation Unsuccessfully!!!")
             return render(request,'addsubcategory.html',{'form':fm})
    else:
        fm=SubCategoryForm()
    return render(request,'addsubcategory.html',{'form':fm})

def subcattable(request):
    cat = Subcategory.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        show=Subcategory.objects.filter(Q(subcategory__icontains=q)|Q(category__icontains=q))
        return render(request,'subcattable.html',{'dat':show})
        
    else: 
     cat = Subcategory.objects.all()
     return render(request,'subcattable.html',{'dat':cat})


def subcat_delete(request,id):
     det = Subcategory.objects.get(pk=id)

     if request.method == 'POST':
	     det.delete()
        
	     return redirect('/subcattable')
     return render (request, 'subcat_delete.html',{'delete':det})


from django.db import connection
import pandas as pd

def test(request):
    return HttpResponse("ghjkm")



def ContactUs(request):
     if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ms=fm.cleaned_data['message']
            
            reg =Contact(name=nm,email=em,message=ms)
            reg.save()
            messages.success(request, "SubCategory Added successfully!")
            return render(request,'index.html')
        else:
             messages.success(request, "Enter vaild details Registation Unsuccessfully!!!")
             return render(request,'Contactus.html',{'form':fm})
     else:
        fm=ContactForm()
     return render(request,'Contactus.html',{'form':fm})


def ContactUsShow(request):
    data = Contact.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
       
        show=Contact.objects.filter(Q(id__icontains=q)|Q(name__icontains=q)|Q(email__icontains=q)|Q(message__icontains=q))
        for s in show:
         return render(request,'Contactshow.html',{'dat':show})
    
    else: 
     data = Contact.objects.all()
     return render(request,'Contactshow.html',{'dat':data})
  




















  