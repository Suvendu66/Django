"""
URL configuration for aptech project.

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

from mysite import views
# from member import views
# from demo import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('savecontact', views.savecontact, name='savecontact'),
    path('details/<int:id>', views.details, name="details"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('updatecontact', views.updatecontact, name="updatecontact"),
    path('admin/', admin.site.urls),
]
