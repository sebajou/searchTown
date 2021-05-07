from django.db import models

# Create your models here.


class CodesPostaux(models.Model):
    codePostal = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'code_postaux'


class Region(models.Model):
    codeRegion = models.IntegerField(primary_key=True)
    nameRegion = models.CharField(max_length=70)

    class Meta:
        managed = True
        db_table = 'Region'


class Departement(models.Model):
    codeDepartement = models.CharField(primary_key=True, max_length=20)
    nameDepartement = models.IntegerField()
    codeRegion = models.ForeignKey(Region, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'Departement'


class Town(models.Model):
    codeTown = models.IntegerField(primary_key=True)
    nameTown = models.CharField(max_length=70)
    centerCoordinateLat = models.IntegerField()
    centerCoordinateLong = models.IntegerField()
    surface = models.IntegerField()
    population = models.IntegerField()
    townPostalcode = models.ManyToManyField(CodesPostaux)
    codeRegion = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    codeDepartement = models.ForeignKey(Departement, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'town'
