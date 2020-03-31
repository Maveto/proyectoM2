"""M2 URL Configuration

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
from django.urls import path, re_path, include
from app import views
from django.conf import settings
from django.views.static import serve
"""from django.conf.urls import handler404, handler500

handler404 = 'app.views.error404'
handler500 = 'app.views.error500'"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', views.index, name='index'),
    path('courses/', views.courses, name='curso'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('accounts/register/', views.register, name='register'),
    re_path(r'^detalle_curso/(?P<curso>.*)/$', views.curso_info, name='curso_info'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
]

'''path('accounts/login/', views.login, name='login'),
 path('accounts/register/index', views.index, name='index'),'''
