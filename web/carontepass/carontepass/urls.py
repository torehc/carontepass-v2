"""carontepass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from access.viewsets import UserViewSet, DeviceViewSet
from access.views import DeviceIDList, homepage, logout_view, personal_info, device_info

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'device', DeviceViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/1/device/(?P<code>.+)$', DeviceIDList.as_view()),
    url(r'^commons/', include('commons.urls')),
    url(r'^accounts/profile/$', homepage, name='homepage'),
    url(r'^accounts/profile/info$', personal_info , name='personal_info'),
    url(r'^accounts/profile/device$', device_info , name='device_info'),
    url(
        r'^$',
        'django.contrib.auth.views.login',
        name='login',
    ),
    url(r'^logout/$',
        logout_view,
        name='logout',
    ),
]