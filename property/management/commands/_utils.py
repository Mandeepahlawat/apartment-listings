from property.models import AreaUnit, HomeType, Listing, ListingData, SaleHistory, ListingTaxInfo
from location.models import City, State, ZipCode
from datetime import datetime
import datetime

def str_to_int(value):
	return int(value or 0)

def str_to_float(value):
	return float(value or 0.0)

def get_price(value):
	if not value:
		return 0.0

	multiplier = {'m': 1000000, 'k': 1000}

	if value.startswith('$'):
		value = value[1:]

	unit = value[-1].lower()

	# if valid unit then truncate last digit
	if unit in multiplier:
		value = value[:-1]
	elif not unit.isdigit():
		print("----> Don't know how to convert this price value <----")
		return 0

	return float(value) * multiplier.get(unit, 1)

def get_date(value):
	if not value:
		return None
	return datetime.datetime.strptime(value, "%m/%d/%Y").date()



