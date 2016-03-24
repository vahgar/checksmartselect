from django.db import models
from smart_selects.db_fields import ChainedForeignKey 

# Create your models here.
class Continent(models.Model):
        name = models.CharField(max_length=255)

        def __str__(self):
        	return self.name

class Country(models.Model):
        continent = models.ForeignKey(Continent)
        name = models.CharField(max_length=255)

        def __str__(self):
        	return self.name

class Location(models.Model):
    continent = models.ForeignKey(Continent)
    country = ChainedForeignKey(
        Country, 
        chained_field="continent",
        chained_model_field="continent", 
        show_all=False, 
        auto_choose=True,
    )
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)

    def __str__(self):
        	return self.street
