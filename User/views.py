from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.
def Login(request):
    if request.method=="POST":
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")
        admincount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()

        if admincount>0:
            admin=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session["aid"] = admin.id
            return redirect("webadmin:HomePage")
        else:
            return render(request,"User/Login.html",{'msg':'Incorrect Credentials'})
    else:
        return render(request,"User/Login.html")
    

def HomePage(request):
    return render(request,"User/Homepage.html")