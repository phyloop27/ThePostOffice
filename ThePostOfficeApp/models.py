from django.db import models

class Name(models.Model):
    identifier = models.AutoField(primary_key=True, db_column='identifier')
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'name'

    def __str__(self):
        return (
            f"{self.first_name}"
            f" {self.last_name}")


class Address(models.Model):
    name = models.OneToOneField(Name,on_delete=models.CASCADE,primary_key=True,related_name="address", db_column='name')
    house_no = models.IntegerField(blank=True, null=True)
    house_name = models.CharField(max_length=120, blank=True, null=True)
    street = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'address'

    def __str__(self):
        return (
            f"{self.name},"
            f"{self.house_no},"
            f"{self.house_name},"
            f"{self.street},"
            f"{self.town}"
            f"{self.post_code}")


class Letter(models.Model):
    letters_pk = models.OneToOneField(Name,on_delete=models.CASCADE,primary_key=True,related_name="letters", db_column='letters_pk')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="letters", db_column='address')
    letter_sent = models.DateField(blank=True, null=True)
    class_field = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'letter'

    def __str__(self):
        return (
            f"{self.letters_pk},"
            f"{self.address},"
            f"{self.letter_sent}"
            f"{self.class_field}")


class Parcel(models.Model):
    parcels_pk = models.OneToOneField(Name,on_delete=models.CASCADE,primary_key=True,related_name="parcels", db_column='parcels_pk')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="parcels", db_column='address')
    courier = models.CharField(max_length=20, blank=True, null=True)
    parcel_sent = models.DateField(blank=True, null=True)
    service = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'parcel'

    def __str__(self):
        return (
            f"{self.parcels_pk},"
            f"{self.address},"
            f"{self.courier}"
            f"{self.parcel_sent}"
            f"{self.service}"
            f"{self.weight}")



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

