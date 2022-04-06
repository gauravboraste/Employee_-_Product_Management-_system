"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login1 import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('registers',views.registers,name="registers"),
    path('login/',views.loginin,name="login"),
    path('profile/',login_required(views.profile),name='profile'),
    path('logout/',views.logoutuser,name='logout'),
    path('adminprofile/',views.adminprofile,name='adminprofile'),
    path('export_excel',views.emp_export_excel,name='export-excel'),
    path('showdata',views.emp_showdata,name='showdata'),
    path('delete_items/<int:pk>/', views.delete_items, name="delete_items"),
    path('Delete/<int:id>/',views.delete_items,name='delete-data'),
    path('<int:id>/',views.update_data,name='update-data'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
    path('product_registation',views.product_register,name='product_registation'),
   
    path('cat_product',views.cat_product,name="cat_product"),
    path('catshow/',views.catshow,name="catshow"),
    path('pro_export',views.pro_export,name='pro_export'),
 
    path('productdelete/<int:id>/',views.productdelete,name='productdelete'),
    path('productupdate/<int:id>/',views.productupdate,name='productupdate'),

    path('catdelete/<int:id>/',views.catdelete,name='catdelete'),
    #path('catupdate/<int:id>/',views.catupdate,name='catupdate'),
    path('addsubcategory/',views.addsubcategory,name='addsubcategory'),
    path('productshow',views.productshow,name='productshow'),
    path('subcattable/',views.subcattable,name='subcattable'),
    path('subcat_delete/<int:id>/',views.subcat_delete,name='subcat_delete'),
    path('test',views.test,name='test'),
    path('contactus',views.ContactUs,name='contactus'),
      path('contactusshow',views.ContactUsShow,name='contactusshow'),

]
