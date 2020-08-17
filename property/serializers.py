from property.models import AreaUnit, HomeType, Listing, ListingData, SaleHistory, ListingTaxInfo
from rest_framework import serializers

class ListingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Listing
		fields = '__all__'


class ListingDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = ListingData
		fields = '__all__'


class AreaUnitSerializer(serializers.ModelSerializer):

	class Meta:
		model = AreaUnit
		fields = '__all__'


class HomeTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = HomeType
		fields = '__all__'


class SaleHistorySerializer(serializers.ModelSerializer):

	class Meta:
		model = SaleHistory
		fields = '__all__'


class ListingTaxInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = ListingTaxInfo
		fields = '__all__'