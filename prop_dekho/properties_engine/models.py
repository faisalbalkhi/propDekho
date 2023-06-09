from django.db import models
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def _str_(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(max_length=200)

    def _str_(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=200)

    def _str_(self):
        return self.name


class Amenities(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Property(TimeStampedModel):
    cartegory = models.ManyToManyField(Category, related_name="property_category")
    feature_image = models.ImageField("Feature Image", upload_to='property/feature_image/')
    location = models.CharField(max_length=200,null=True,blank=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='property_type',null=True, blank=True)
    price = models.FloatField()
    maintainance_charges = models.FloatField(null=True,blank=True)
    no_of_bedroom = models.IntegerField("Number of Bedroom", null=True, blank=True)
    no_of_bathroom = models.IntegerField("Number of Bathroom", null=True, blank=True)
    no_of_kitchen = models.IntegerField("Number of Kitchen", null=True, blank=True)
    author_image = models.ImageField("Author Image", null=True, blank=True, upload_to='property/author_image/')
    author_name = models.CharField("Author Name", max_length=233, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    area = models.IntegerField()
   


    def _str_(self):
        return self. author_name


class PgFacility(models.Model):
    name = models.CharField(max_length=100)
    facility_type = models.BooleanField(default=0)

    def _str_(self):
        return self.name


class PgType(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


KEY_FACILITIES = [
    (True, "Yes"),
    (False, "No"),
]


class LatestPg(models.Model):
    pg_image = models.ImageField('Pg Image', upload_to='latestpg/latestpg_image/')
    pg_location = models.CharField(max_length=255)
    pg_rent = models.FloatField()
    pg_name = models.CharField(max_length=255)
    pgtype = models.ManyToManyField(PgType, related_name='pg_type')
    # pg_facility = models.ManyToManyField(PgFacility, related_name='pgfacility')
    ac = models.BooleanField(choices=KEY_FACILITIES)
    washroom = models.BooleanField(choices=KEY_FACILITIES)
    dth = models.BooleanField(choices=KEY_FACILITIES)
    wifi = models.BooleanField(choices=KEY_FACILITIES)
    matress = models.BooleanField(choices=KEY_FACILITIES)
    cupboard = models.BooleanField(choices=KEY_FACILITIES)
    side_table = models.BooleanField(choices=KEY_FACILITIES)
    balcony = models.BooleanField(choices=KEY_FACILITIES)

    def _str_(self):
        return self.pg_name


FLAT_TYPE = [
    (1, '1BHK'),
    (2, '2BHK'),
    (3, '3BHK'),
    (4, '4BHK'),
]


class LatesFlat(models.Model):
    flat_name = models.IntegerField(choices=FLAT_TYPE)
    flat_image = models.ImageField("Flat Image", upload_to='latest/flat_image/')
    flat_rent = models.CharField(max_length=200)
    area = models.IntegerField()
    flat_location = models.CharField(max_length=200)

    def _str_(self):
        return self.flat_name


class PropertyForSale(models.Model):
    property_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    sale_image = models.ImageField("Sale Image", upload_to='propertysale/sale_image')
    sale_price = models.FloatField()
    sale_address = models.CharField(max_length=200)
    sale_area = models.IntegerField()

    def _str_(self):
        return self.property_name