from django.db import models

# Create your models here.
class Person(models.Model):
    """ Person class"""
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70)
    surname_name = models.CharField(max_length=70)
    maiden_name = models.CharField(max_length=70)
    create_date = models.DateTimeField('date created', auto_created=True)
    academic_level = models.CharField(max_length=100)

    def __str__(self):
        """Return resonable name"""
        var_name = self.first_name + self.surname_name
        return var_name;

class Address(models.Model):
    """"""
    House_number = models.IntegerField()
    street_name = models.CharField(max_length=200)
