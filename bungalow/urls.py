"""bungalow URL Configuration

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

from rest_framework import routers

from property.views import (
	ListingViewSet, ListingDataViewSet, AreaUnitViewSet, HomeTypeViewSet, SaleHistoryViewSet, ListingTaxInfoViewSet
)

from location.views import StateViewSet, CityViewSet, ZipCodeViewSet

router = routers.DefaultRouter()
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'zip-codes', ZipCodeViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'listings-data', ListingDataViewSet)
router.register(r'area-units', AreaUnitViewSet)
router.register(r'home-types', HomeTypeViewSet)
router.register(r'sale-histories', SaleHistoryViewSet)
router.register(r'listing-tax-info', ListingTaxInfoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
