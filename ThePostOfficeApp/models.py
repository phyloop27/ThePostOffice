# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Names(models.Model):
    nam_identifier = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'names'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    nam_identifier = models.ForeignKey('Names', models.DO_NOTHING, db_column='nam_identifier', blank=True, null=True)
    house_no = models.IntegerField(blank=True, null=True)
    house_name = models.CharField(max_length=120, blank=True, null=True)
    street = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=12, blank=True, null=True)
    date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = True
        db_table = 'address'

    def __str__(self):
        return f"{self.house_no} {self.house_name} {self.street} {self.town} {self.post_code} {self.date_field}"



class Letters(models.Model):
    letters_pk = models.AutoField(primary_key=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    letter_sent = models.DateField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'letters'

    def __str__(self):
        return f"{self.address} {self.letter_sent} {self.class_field}"


class Courier(models.Model):
    courier_id = models.IntegerField(primary_key=True)
    courier_name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'courier'

    def __str__(self):
        return f"{self.courier_name} {self.courier_id}"


class Parcels(models.Model):
    parcels_pk = models.AutoField(primary_key=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    courier = models.ForeignKey(Courier, models.DO_NOTHING, blank=True, null=True)
    parcel_sent = models.DateField(blank=True, null=True)
    service = models.CharField(max_length=8, blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'parcels'

    def __str__(self):
        return f"{self.address} {self.courier} {self.parcel_sent} {self.service} {self.weight}"


class PostOfficeSales(models.Model):
    office_date = models.DateField(blank=True, null=True)
    post_office_id = models.IntegerField(primary_key=True)
    first_class_stamp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    sec_class_stamp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    letters_postage_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    standard_parcel = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    next_day_parcel = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    tot_kg_price = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'post_office_sales'

    def __str__(self):
        return f"{self.office_date} {self.first_class_stamp} {self.sec_class_stamp} {self.letters_postage_cost} {self.standard_parcel} {self.next_day_parcel} {self.tot_kg_price}"


class Prices(models.Model):
    prices_pk = models.AutoField(primary_key=True)
    first_cl_stamp = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sec_cl_stamp = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    post_letter = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    standard_parcel = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    next_day_parcel = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    price_per_kg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prices_fk = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'prices'

    def __str__(self):
        return f"{self.first_cl_stamp} {self.sec_cl_stamp} {self.post_letter} {self.standard_parcel} {self.next_day_parcel} {self.price_per_kg}"


class Quantity(models.Model):
    quantity_pk = models.AutoField(primary_key=True)
    date_field = models.DateField(db_column='date_', unique=True, blank=True, null=True)  # Field renamed because it ended with '_'.
    first_cl_stamp = models.IntegerField()
    sec_cl_stamp = models.IntegerField()
    post_letter = models.IntegerField()
    standard_parcel = models.IntegerField()
    next_day_parcel = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'quantity'

    def __str__(self):
        return f"{self.date_field} {self.first_cl_stamp} {self.sec_cl_stamp} {self.post_letter} {self.standard_parcel} {self.next_day_parcel} {self.weight}"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
