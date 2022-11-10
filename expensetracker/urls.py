"""expensetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myApp import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', v1.dashboard, name='dashboard'),
    path('', v1.LoginPage, name='login'),
    path('logout/', v1.LogoutPage, name='logout'),
    path('signup/', v1.SignupPage, name='signup'),
    path('about/', v1.about, name='about'),
    path('signup/signupdata/', v1.signupdata, name='signupdata'),
    path('signindata/', v1.signindata, name='signindata'),
    path('signindata/signindata', v1.signindata, name='signindata2'),
    path('saveexpense/', v1.saveexpense, name='saveexpense'),
    path('saveexpense/saveexpensedata/', v1.saveexpensedata, name='saveexpensedata'),
    path('saveincome/', v1.saveincome, name='saveincome'),
    path('saveincome/saveincomedata/', v1.saveincomedata, name='saveincomedata'),
    path('viewexpense/', v1.viewexpense, name='viewexpense'),
    path('deleteexpense/<int:id>', v1.deleteexpense, name='deleteexpense'), 
    path('viewincome/', v1.viewincome, name='viewincome'),
    path('deleteincome/<int:id>', v1.deleteincome, name='deleteincome'),
    path('searchexpensedata/<int:id>', v1.searchexpensedata, name='searchexpensedata'),
    path('saveeditexpense', v1.saveeditexpense, name='saveeditexpense'),
    path('searchincomedata/<int:id>', v1.searchincomedata, name='searchincomedata'),
    path('saveeditincome', v1.saveeditincome, name='saveeditincome'),
    path('sortbydate', v1.sortbydate, name='sortbydate'),
    path('sortbydate2', v1.sortbydate2, name='sortbydate2'),
    path('sortbyamt', v1.sortbyamt, name='sortbyamt'),
    path('sortbyamt2', v1.sortbyamt2, name='sortbyamt2'),
    path('sortbydateincome', v1.sortbydateincome, name='sortbydateincome'),
    path('sortbydateincome2', v1.sortbydateincome2, name='sortbydateincome2'),
    path('sortbyamtincome', v1.sortbyamtincome, name='sortbyamtincome'),
    path('sortbyamtincome2', v1.sortbyamtincome2, name='sortbyamtincome2'),
    path('expensecatfood', v1.expensecatfood, name='expensecatfood'),
    path('expensecattravel', v1. expensecattravel, name='expensecattravel'),
    path('expensecatdonation', v1.expensecatdonation, name='expensecatdonation'),
    path('expensecatother', v1.expensecatother, name='expensecatother'),
    path('incomecatbuss', v1.incomecatbuss, name='incomecatbuss'),
    path('incomecatfreela', v1.incomecatfreela, name='incomecatfreela'),
    path('incomecatsalary', v1.incomecatsalary, name='incomecatsalary'),
    path('incomecatother', v1.incomecatother, name='incomecatother'),
]
