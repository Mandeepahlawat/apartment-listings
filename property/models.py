from django.db import models
from location.models import State, City, ZipCode

class AreaUnit(models.Model):
	unit = models.CharField(max_length=10)

	def __str__(self):
		return self.unit


class HomeType(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name


class Listing(models.Model):
	bathrooms = models.DecimalField(max_digits=4, default=0.0, decimal_places=1)
	bedrooms = models.IntegerField(default=0)
	home_type = models.ForeignKey('HomeType', on_delete=models.DO_NOTHING)
	year_built = models.IntegerField(null=True)
	area_unit = models.ForeignKey('AreaUnit', on_delete=models.DO_NOTHING)
	home_size = models.IntegerField(blank=True)
	property_size = models.IntegerField(blank=True)
	price = models.DecimalField(max_digits=20, default=0.0, decimal_places=3)
	address = models.CharField(max_length=200)
	city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
	state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
	zip_code = models.ForeignKey(ZipCode, on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = [['address', 'city', 'state', 'zip_code']]
	
	def __str__(self):
		return f'{self.address}-{self.city}-{self.state}-{self.zip_code}'


class ListingData(models.Model):

	SOURCE_TYPES = [
		("zillow", "Zillow")
	]

	listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
	external_id = models.CharField(max_length=200)
	external_link = models.URLField()
	source = models.CharField(max_length=100, choices=SOURCE_TYPES, default="zillow")
	rent_price = models.DecimalField(max_digits=20, default=0.0, decimal_places=3, blank=True, null=True)
	# corresponds to rentzestimate_amount
	estimated_rent = models.DecimalField(max_digits=20, default=0.0, decimal_places=3, blank=True, null=True)
	# corresponds to rentzestimate_last_updated
	estimated_rent_updated = models.DateField(blank=True, null=True)
	# corresponds to zestimate_amount
	estimated_sale_price = models.DecimalField(max_digits=20, default=0.0, decimal_places=3, blank=True, null=True)
	# corresponds to zestimate_last_updated
	estimated_sale_price_updated = models.DateField(blank=True, null=True)


class SaleHistory(models.Model):
	listing = models.ForeignKey('Listing', on_delete=models.DO_NOTHING)
	sold_date = models.DateField(null=True)
	sold_price = models.DecimalField(max_digits=20, default=0.0, decimal_places=3)

	def __str__(self):
		return f'{self.listing}-{self.sold_date}-{self.sold_price}'


class ListingTaxInfo(models.Model):
	year = models.IntegerField()
	amount = models.DecimalField(null=True, decimal_places=2, max_digits=10)
	listing = models.ForeignKey('Listing', on_delete=models.CASCADE)

	class Meta:
		unique_together = ["year", "listing"]

	def __str__(self):
		return f'{self.listing}-{self.year}-{self.amount}'
