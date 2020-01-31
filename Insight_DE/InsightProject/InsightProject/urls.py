"""InsightProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.conf.urls import url, include
from django.contrib import admin
# from datapea.serializers import ProvidersViewSet, DrugsViewSet
from rest_framework import routers
from django.urls import path, include

# router = routers.DefaultRouter()
# router.register(r'api/v1/providers', ProvidersViewSet)
# router.register(r'api/v1/drugs', DrugsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'^', include(router.urls)),
    path('', include('datapea.urls')),
]
