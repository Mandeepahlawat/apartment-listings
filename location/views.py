from location.models import ZipCode, State, City
from location.serializers import StateSerializer, CitySerializer, ZipCodeSerializer
from rest_framework import viewsets

class StateViewSet(viewsets.ModelViewSet):
	queryset = State.objects.all()
	serializer_class = StateSerializer


class CityViewSet(viewsets.ModelViewSet):
	queryset = City.objects.all()
	serializer_class = CitySerializer


class ZipCodeViewSet(viewsets.ModelViewSet):
	queryset = ZipCode.objects.all()
	serializer_class = ZipCodeSerializer
