from django.contrib import admin
from .models import Contact, Employee, ITCategory,Productdb,Subcategory

# Register your models here.
@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','username','email','password','is_superuser')

@admin.register(Productdb)
class Productdb(admin.ModelAdmin):
    list_display = ('pid','category','product_name','product_brand','serial_no','model_no','description')

@admin.register(ITCategory)
class ITCategory(admin.ModelAdmin):
    list_display = ('category',)

@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin):
    list_display = ('subcategory','category',)

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name','email','message')

