from location.models import ZipCode, State, City
from rest_framework import serializers

class StateSerializer(serializers.ModelSerializer):

	class Meta:
		model = State
		fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City
		fields = '__all__'


class ZipCodeSerializer(serializers.ModelSerializer):

	class Meta:
		model = ZipCode
		fields = '__all__'