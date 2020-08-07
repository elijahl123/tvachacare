"""TvachaCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from patientInformation import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-console'),
    path('', views.index, name='home'),
    path('login/', views.loginPage, name="login"),
    path('login/admin/', views.loginadmin, name="loginAdmin"),
    path('addpatient/', views.addpatient, name='addPatient'),
    path('logout', views.logout, name='logout'),
    path('patient/<slug>/', views.patient_page, name='patient_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)