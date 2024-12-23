"""
URL configuration for RecursosHumanosProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from EmpleadosApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleado/', empleadoView),
    path('empleadoV2/', empleado2View),
    path('empleadosAPI/', empleados_list),
    path('empleadosAPI/<int:pk>/', empleado_detail),
    path('cEmpleadosAPI/', EmpleadoList.as_view()),
    path('cEmpleadosAPI/<int:pk>/', EmpleadoDetail.as_view()),
]
