from django.urls import path,include

from Admin import views
app_name="webadmin"
urlpatterns = [
    path('HomePage',views.HomePage,name="HomePage"),
    path("Certificate/",views.Certificate,name="Certificate"),
    path("delCertificate/<int:did>",views.delCertificate,name="delCertificate"),
    path("upCertificate/<int:cid>",views.upCertificate,name="upCertificate"),

    path("Service/",views.Service,name="Service"),
    path("delService/<int:did>",views.delService,name="delService"),
    path("upService/<int:eid>",views.upService,name="upService"),

    path("Documents/",views.Documents,name="Documents"),
    path("delDocument/<int:did>",views.delDocument,name="delDocument"),
    path("upDocument/<int:eid>",views.upDocument,name="upDocument"),
    path('AjaxService/',views.AjaxService,name="AjaxService"),

]