<<<<<<< HEAD
"""stdproctor URL Configuration

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
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from student import views
from django.conf.urls import include,url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),

    path('barchart/', include('student.urls')),
    url(r'mplimage.png',views.plotbar),
    #Authentication ke view
    path('accounts/',include('accounts.urls')),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    #Page 3
    path('mathematics/',views.maths,name="maths"),
    path('physics/',views.phy, name="phy"),
    path('chemistry/',views.chem,name="chem"),
    path('spa/',views.spa, name="spa"),
    path('ed/', views.ed, name="ed"),
    path('cs/', views.cs, name="cs"),
    path('extra/',views.extra,name="extra"),
    path('graph',views.plotbar, name ="graph"),
    path('graph2',views.plotbar, name ="graph2"),
    path('graph3',views.plotbar, name ="graph3"),
    path('graph4',views.plotbar, name ="graph4"),
    path('graph5',views.plotbar, name ="graph5"),
    path('graph6',views.plotbar, name ="graph6"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
"""stdproctor URL Configuration

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
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from student import views
from django.conf.urls import include,url
import student.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),

    path('barchart/', include('student.urls')),
    url(r'mplimage.png',student.views.plotbar),
    #Authentication ke view
    path('accounts/',include('accounts.urls')),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 14e2b97fafab7d6a3f4be01912e72f0cc611876d
