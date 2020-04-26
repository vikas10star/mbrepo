"""mbproject URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView
from mbapp import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('/', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('home/', views.show_emplist, name='emplist'),
    path('', views.show_emplist, name='emplist'),
    path('addemp/', views.add_emp, name='addemp'),
    path('update_render/<int:emp_id>', views.update_render, name='update_render'),
    path('update_emp/<int:emp_id>', views.update_emp, name='update_emp'),
    path(r'^delete/(?P<emp_id>\d+)/$', views.delete_emp, name='delete_emp'),
    path('signup/',views.signup_view, name='signup'), 
    path('api/', include(router.urls)),    
]
