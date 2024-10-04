from django.urls import path,include

from User import views
app_name="webuser"
urlpatterns = [
    path('Login',views.Login,name="Login"),
    path('HomePage',views.HomePage,name="HomePage"),


]