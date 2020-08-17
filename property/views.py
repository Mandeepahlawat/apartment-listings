from property.models import AreaUnit, HomeType, Listing, ListingData, SaleHistory, ListingTaxInfo
from property.serializers import (
	ListingSerializer, ListingDataSerializer, AreaUnitSerializer, HomeTypeSerializer, SaleHistorySerializer, ListingTaxInfoSerializer
)
from rest_framework import viewsets

class ListingViewSet(viewsets.ModelViewSet):
	queryset = Listing.objects.all()
	serializer_class = ListingSerializer


class ListingDataViewSet(viewsets.ModelViewSet):
	queryset = ListingData.objects.all()
	serializer_class = ListingDataSerializer


class AreaUnitViewSet(viewsets.ModelViewSet):
	queryset = AreaUnit.objects.all()
	serializer_class = AreaUnitSerializer


class HomeTypeViewSet(viewsets.ModelViewSet):
	queryset = HomeType.objects.all()
	serializer_class = HomeTypeSerializer


class SaleHistoryViewSet(viewsets.ModelViewSet):
	queryset = SaleHistory.objects.all()
	serializer_class = SaleHistorySerializer


class ListingTaxInfoViewSet(viewsets.ModelViewSet):
	queryset = ListingTaxInfo.objects.all()
	serializer_class = ListingTaxInfoSerializer

