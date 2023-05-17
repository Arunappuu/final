from django.urls import path

from . import views

app_name='school_app'

urlpatterns = [
    path('', views.add, name='mem'),
    path('dep', views.dpart, name='dep'),
    path('register', views.reg, name='reg'),
    path('login', views.log, name='login'),
    path('logout/', views.logoutfrom, name='logout'),
    path('form', views.show_form, name='show_form'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
    
   
]
 













                
        
    
  
