"""
URL configuration for ThePostOffice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from ThePostOfficeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'), # Remove this On completion!! Change to Login page!!!!
    path('formName/', views.formName, name='formName'),
    path('formAddress/', views.formAddress, name='formAddress'),
    path('formPostage/', views.formPostage, name='formPostage'),
    path('formSuccess', views.formSuccess, name='formSuccess'),
    path('customerDetails/', views.customerDetails, name='customerDetails'),
    path('postedItems', views.postedItems, name='postedItems'),
    path('prices/', views.prices, name='prices'),
    path('postOfficeSales/', views.postOfficeSales, name='postOfficeSales'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]
