from django.db import models
from localflavor.generic.models import IBANField, BICField
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES

# Create your models here.

class UserProfile(models.Model):

    first_name = models.CharField('First name of the user', max_length=100)
    last_name = models.CharField('Lat name of the user', max_length=100)
    iban = IBANField('IBAN of the user', include_countries=IBAN_SEPA_COUNTRIES, default=None)
    image = models.ImageField('Image of the user', upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return "%s" % self.first_name
