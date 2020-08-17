from django.core.management.base import BaseCommand, CommandError
from property.models import AreaUnit, HomeType, Listing, ListingData, SaleHistory, ListingTaxInfo
from location.models import City, State, ZipCode

import os
import csv
from django.conf import settings
from django.db import transaction

from property.management.commands._utils import str_to_int, str_to_float, get_price, get_date



class Command(BaseCommand):
	help = 'Imports data from specified CSV file'

	def add_arguments(self, parser):
		parser.add_argument('filename', type=str, nargs='?', default=f'{settings.BASE_DIR}/challenge_data.csv')

	def handle(self, *args, **options):
		filename = options["filename"]

		if not os.path.exists(filename):
			raise CommandError(f'"{filename}" does not exist')

		with open(filename, 'r') as file:
			reader = csv.DictReader(file)
			for i, row in enumerate(reader):
				self.create_records(row)
				self.stdout.write(f"========created record-{i}=======")

		self.stdout.write(self.style.SUCCESS("Successfully imported all row"))

	def create_records(self, row):
		try:
			with transaction.atomic():
				# create location records
				state, _ = State.objects.get_or_create(name=row.get('state'))
				city, _ = City.objects.get_or_create(name=row.get('city'), state=state)
				zip_code, _ = ZipCode.objects.get_or_create(code=row.get('zipcode'), city=city)

				# create property records
				home_type, _ = HomeType.objects.get_or_create(name=row.get('home_type'))
				area_unit, _ = AreaUnit.objects.get_or_create(unit=row.get('area_unit'))

				listing = Listing(
					bathrooms=str_to_float(row.get('bathrooms')),
					bedrooms=str_to_int(row.get('bedrooms')),
					home_type=home_type,
					year_built=str_to_int(row.get('year_built')),
					area_unit=area_unit,
					home_size=str_to_int(row.get('home_size')),
					property_size=str_to_int(row.get('property_size')),
					price=get_price(row.get('price')),
					address=row.get('address'),
					city=city,
					state=state,
					zip_code=zip_code
				)
				listing.save()


				listing_data = ListingData(
					listing=listing,
					external_id=row.get('zillow_id'),
					external_link=row.get('link'),
					rent_price=get_price(row.get('rent_price')),
					estimated_rent=get_price(row.get('rentzestimate_amount')),
					estimated_rent_updated=get_date(row.get('rentzestimate_last_updated')),
					estimated_sale_price=get_price(row.get('zestimate_amount')),
					estimated_sale_price_updated=get_date(row.get('zestimate_last_updated')),
				)
				listing_data.save()


				listing_tax_info = ListingTaxInfo(
					listing=listing,
					amount=get_price(row.get('tax_value')),
					year=row.get('tax_year'),
				)
				listing_tax_info.save()
				

				sale_history = SaleHistory(
					listing=listing,
					sold_date=get_date(row.get('last_sold_date')),
					sold_price=get_price(row.get('last_sold_price')),
				)
				sale_history.save()
		except Exception as e:
			self.stdout.write("Skipping row due to error", row, e)
