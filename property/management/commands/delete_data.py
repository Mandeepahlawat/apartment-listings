from django.core.management.base import BaseCommand, CommandError
from property.models import AreaUnit, HomeType, Listing, ListingData, SaleHistory, ListingTaxInfo
from location.models import City, State, ZipCode


class Command(BaseCommand):
	help = "Empties the Database"

	def handle(self, *args, **options):
		ListingData.objects.all().delete()
		ListingTaxInfo.objects.all().delete()
		SaleHistory.objects.all().delete()
		Listing.objects.all().delete()
		HomeType.objects.all().delete()
		AreaUnit.objects.all().delete()