from django.db import models

# Create your models here.
class tbl_certificate(models.Model):
    certificate_name=models.CharField(max_length=50)

class tbl_service(models.Model):
    certificate=models.ForeignKey(tbl_certificate,on_delete=models.CASCADE)
    service_name=models.CharField(max_length=50)
    service_charge=models.CharField(max_length=10)
    service_discription=models.CharField(max_length=500)


class tbl_documents(models.Model):
    certificate=models.ForeignKey(tbl_certificate,on_delete=models.CASCADE)
    service=models.ForeignKey(tbl_service,on_delete=models.CASCADE)
    documents_name=models.CharField(max_length=100)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)