"""
URL configuration for industary project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
from rest_framework.routers import DefaultRouter
DRO=DefaultRouter()
DRO.register('list',ActorsData,basename='ActorsData')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('registration/',registration,name='registration'),
    path('login_user/',login_user,name='login_user'),
    path('logout_user/',logout_user,name='logout_user'),
    path('app/',include(DRO.urls)),
    path('hello/',hello.as_view(),name='hello'),
    path('conform_logout/',conform_logout,name='conform_logout'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
