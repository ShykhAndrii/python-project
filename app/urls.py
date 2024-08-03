"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, re_path
from main import views as main

product_patterns = [
    path("", main.products),
    path("comments", main.comments),
    path("questions", main.questions),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', main.index, name='home'),
    path('about', main.about, name='about'),
    re_path(r'^contact', main.contact),
    #re_path('parametr', main.param, kwargs={"name":"Roza", "age":"34"}),
    path("products/<int:id>", include(product_patterns)),
    path('parametr/<name>/<int:age>', main.param1),
    
]
