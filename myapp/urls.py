
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('doctor/', views.doctor, name='doctor'),
    path('myservice/', views.myservice, name='myservice'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete,),
    path('contact/', views.contact, name='contact'),
    path('edit/<int:id>', views.edit, name='edit'),
]
