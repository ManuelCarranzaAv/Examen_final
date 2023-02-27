"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from prueba.views import inicio
from prueba.views import nosotros,vision,aplicaciones


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('vision/', vision,name='vision'),
    path('aplicaciones/', aplicaciones,name='aplicaciones')
]
#vistas globales
#vistas locales
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)