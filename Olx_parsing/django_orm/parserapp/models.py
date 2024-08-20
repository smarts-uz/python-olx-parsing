from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    category_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Category'

class Moda_stil(models.Model):
    id = models.AutoField(primary_key=True)
    Cust

