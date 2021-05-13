# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    urlh = models.CharField(max_length=50)
    status = models.IntegerField(blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    product_type = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    source = models.CharField(max_length=100)
    seller = models.CharField(max_length=200, blank=True, null=True)
    crawl_date = models.DateField()
    crawl_time = models.DateTimeField()
    mrp = models.FloatField()
    available_price = models.FloatField()
    discount = models.FloatField()
    stock = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'products'
