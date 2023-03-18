"""API_SDN01 URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from api_staf import api_views as staff_views
from api_guru import api_views as guru_views
from api_siswa import api_views as siswa_views


router = routers.DefaultRouter()
router.register(r'staff', staff_views.StaffViewSets)
router.register(r'kelas', staff_views.KelasViewsets)

router.register(r'mapel', guru_views.MapelViewsets)
router.register(r'guru', guru_views.GuruViewSets)
router.register(r'mapel_guru', guru_views.MapelGuruViewsets)

router.register(r'siswa', siswa_views.SiswaViewSets)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
