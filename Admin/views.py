from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.
def HomePage(request):
    certificate=tbl_certificate.objects.all()
    service=tbl_service.objects.all()
    documents=tbl_documents.objects.all()
    return render(request,"Admin/Homepage.html",{"certificate":certificate})


def Certificate(request):
    certificate=tbl_certificate.objects.all()
    if request.method == "POST":
        tbl_certificate.objects.create(certificate_name=request.POST.get("txt_certificate"))
        return render(request,"Admin/Certificate.html",{"certificate":certificate})
    else:
        return render(request,"Admin/Certificate.html",{"certificate":certificate})
    


def delCertificate(request,did):
    tbl_certificate.objects.get(id=did).delete()
    return redirect("webadmin:Certificate")





def upCertificate(request,cid):
    data=tbl_certificate.objects.get(id=cid)
    if request.method=="POST":
        data.certificate_name=request.POST.get("txt_certificate")
        data.save()
        return redirect("webadmin:Certificate")
    else:
        return render(request,"Admin/Certificate.html",{"cid":data})
    









def Service(request):
        certificate=tbl_certificate.objects.all()
        service=tbl_service.objects.all()
        if request.method == "POST":
            certificate=tbl_certificate.objects.get(id=request.POST.get("txt_certificate"))
            tbl_service.objects.create(service_name=request.POST.get("txt_service"),
                                       service_charge=request.POST.get("txt_service_charge"),
                                       service_discription=request.POST.get("txt_service_discription"),
                                       certificate=certificate)
            return redirect("webadmin:Service")
        else:
            return render(request,"Admin/Service.html",{"service":service,"certificate":certificate})



def delService(request,did):
    tbl_service.objects.get(id=did).delete()
    return redirect("webadmin:Service")





def upService(request,eid):
    data=tbl_service.objects.get(id=eid)
    if request.method=="POST":
        data.service_name=request.POST.get("txt_service")
        data.service_charge=request.POST.get("txt_service_charge")
        data.service_discription=request.POST.get("txt_service_discription")
        data.save()
        return redirect("webadmin:Service")
    else:
        return render(request,"Admin/Service.html",{"sis":data})
    







def Documents(request):
    certificate=tbl_certificate.objects.all()
    service=tbl_service.objects.all()
    documents=tbl_documents.objects.all()
    if request.method == "POST":
        certificate=tbl_certificate.objects.get(id=request.POST.get("txt_certificate"))
        service=tbl_service.objects.get(id=request.POST.get("txt_service"))
        tbl_documents.objects.create(documents_name=request.POST.get("txt_documents"),
                                     certificate=certificate,
                                       service=service)
        return redirect("webadmin:Documents")
    else:
        return render(request,"Admin/Documents.html",{"documents":documents,"service":service,"certificate":certificate})
    






def delDocument(request,did):
    tbl_documents.objects.get(id=did).delete()
    return redirect("webadmin:Documents")





def upDocument(request,eid):
    data=tbl_documents.objects.get(id=eid)
    if request.method=="POST":
        data.documents_name=request.POST.get("txt_documents")
        data.save()
        return redirect("webadmin:Documents")
    else:
        return render(request,"Admin/Documents.html",{"dis":data})
    


def AjaxService(request):
    certificate=tbl_certificate.objects.get(id=request.GET.get("certificateid"))
    service=tbl_service.objects.filter(certificate=certificate)
    return render(request,"Admin/AjaxService.html",{"service":service})