"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import  *
from django.contrib import admin
from django.urls import path
from myfunctions import  *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one', one),
    path('',home),
    path('home',home),
    path('login',login),
    path('course',course),
    path('navbr',navbr),
    path('courses',courses),
    path('fpass',fpass),
    path('forget',forget),
    path('forg',forg),
    path('fo',fo),
    path('ahome',ahome),
    path('cart',cart),
    path("acourse",acourse),
    path("dcourse", dcourse),
    path("courses", courses),
    path("display",display),
   # path("bcourse",bcourse),
    path('imgexample',imgexample),
    # path('imge',imge),
path('move',move),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
