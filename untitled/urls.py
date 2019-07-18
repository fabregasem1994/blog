"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from posts.views import index,blog,post,search,post_create,post_delete,post_update,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/',blog,name='post-list'),
    path('post/<id>/',post,name='post-detail'),
    path('search/',search,name='search'),
    path('tinymce/',include('tinymce.urls')),
    path('create/',post_create,name='post-create'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete', post_delete, name='post-delete'),
    path('accounts/login/', login),
    path('accounts/', include('allauth.urls')),

]
