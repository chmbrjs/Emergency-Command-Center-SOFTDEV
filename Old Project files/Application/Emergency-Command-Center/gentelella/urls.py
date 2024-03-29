"""gentelella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from gentelella.core import views
from gentelella.core.views import index

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.LoginPageView, name='login'),
    url(r'^dead-and-missing/', views.dead, name='dead'),
    url(r'^local-government-agency/', views.LGAPageView, name='lga'),
    url(r'^non-govt-organization/', views.NGOPageView, name='ngo'),
    url(r'^statistics-overview/', views.SOPageView, name='stats'),
    url(r'^casualties/', views.CasualtiesPageView, name='casualties'),
    url(r'^calamity-level-scheme/', views.CLPageView, name='calamity'),
    url(r'^register-user/', views.RegisterPageView, name='register'),
    url(r'^auth-user-session/', views.LoginAuthPageView, name='login-auth')
]
