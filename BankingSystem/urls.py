from django.urls import path
from . import views

app_name = 'BankingSystem'
urlpatterns = [
     path('',views.index,name='index'),
     path('deposit/',views.deposit,name='deposit'),
     path('userinfo/',views.userinfo,name='userinfo'),
     path('withdraw/',views.withdraw,name='withdraw'),
     path('sendmoney/',views.sendmoney,name='sendmoney'),
     path('home/<int:pk>/',views.home,name='home'),
     path('adduser/',views.adduser,name='adduser'),

]