"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
urlpatterns = [
    path('', views.add,name='home'),
    # path('details',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListview.as_view(),name='cbvhome'),
     path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
     path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
     path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),


]
