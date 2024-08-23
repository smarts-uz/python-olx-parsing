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
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Moda_stil'


class Bolalar_dunyosi(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Bolalar_dunyosi'


class Kochmas_mulk(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Kochmas_mulk'


class Transport(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Transport'


class Ish(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ish'


class Hayvonlar(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Hayvonlar'


class Uy_va_Bog(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Uy va Bog'


class Elektronika(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Elektronika'


class Biznes_va_Xizmatlar(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Biznes_va_Xizmatlar'


class Xobbi_va_Sport(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Xobi va Sport'


class Tekinga_berish(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tekinga berish'


class Ayirboshlash(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    product_image_path = models.CharField(max_length=255, blank=True, null=True)
    add_product_time = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ayirboshlash'
