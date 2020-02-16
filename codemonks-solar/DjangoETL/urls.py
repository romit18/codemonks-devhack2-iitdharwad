"""DjangoETL URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from firstapp.views import index
from django.conf import settings 
from django.conf.urls.static import static 
from firstapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('services/',services,name="services"),
    path('signup/',signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('selectionday/',about,name='blog1'),
    path('sacred/',about1,name='blog2'),
    path('shark/',about2,name='blog3'),
    path('episodes/',epi,name='blog4'),
    path('profile/',profile,name='blog5'),
    url(r'^delete/(?P<username>[\w|\W.-]+)/$', delete_user, name='delete-user'),
    path('image_upload/', maps_image_view, name = 'maps_image_view'), 
    path('dash/',dash,name='dash'),
    # path('success', success, name = 'success'),
    # path('process_image',processImage, name='processImage'),

    path('result/(?P<response>\d+)/$',result,name='result'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
