from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Property(models.Model):
    cartegory = models.ManyToManyField(Category, related_name="property_category")
    feature_image = models.ImageField("Feature Image", upload_to='property/feature_image/')
    location = models.CharField(max_length=200)
    title = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    price = models.FloatField()
    li_title1 = RichTextField()
    no_of_bedroom = models.IntegerField("Number of Bedroom", null=True, blank=True)
    li_title2 = RichTextField()
    no_of_bathroom = models.IntegerField("Number of Bathroom", null=True, blank=True)
    li_title3 = RichTextField()
    no_of_kitchen = models.IntegerField("Number of Kitchen", null=True, blank=True)
    author_image = models.ImageField("Author Image", null=True, blank=True, upload_to='property/author_image/')
    author_name = models.CharField("Author Name", max_length=233, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title.name


class PgFacility(models.Model):
    ac = models.CharField(max_length=200)
    washroom = models.CharField(max_length=200)
    Balcony = models.CharField(max_length=200)
    cupboard = models.CharField(max_length=200)
    tv = models.CharField(max_length=200)
    dth = models.CharField(max_length=200)
    wifi = models.CharField(max_length=200)
    side_table = models.CharField(max_length=200)
    mattress = models.CharField(max_length=200)


class Latestpg(models.Model):
    PG_CHOICES = [
        ('for girls&boys', 'for girls&boys'),
        ('All prepared', 'All prepared'),
    ]
    pg_image = models.ImageField('Pg Image', upload_to='latestpg/latestpg_image/')
    pg_location = models.CharField(max_length=255)
    pg_rent = models.FloatField()
    pg_name = models.CharField(max_length=255)
    pgtype = models.CharField(choices=PG_CHOICES, max_length=20)






