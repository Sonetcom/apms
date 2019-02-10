from django.db import models

# Create your models here.
class Person(models.Model):
    """ Person class"""

    # Personal Data 
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70)
    surname_name = models.CharField(max_length=70)
    maiden_name = models.CharField(max_length=70)
    date_of_birth = models.DateTimeField()
    create_date = models.DateTimeField('date created', auto_created=True)
    academic_level = models.CharField(max_length=100)

    # contact details
    work_number = models.IntegerField()
    home_number = models.IntegerField()
    cell_number = models.IntegerField()



    def __str__(self):
        """Return resonable name"""
        var_name = self.first_name + self.surname_name
        return var_name;

#=============================================================
#      Address to Store address of users
#=============================================================

class Address(models.Model):
    """"""
    house_number = models.IntegerField()
    street_name = models.CharField(max_length=200)
    post_code = models.CharField(max_length=70)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        """"""
        var_name = self.house_number + self.street_name 

    def __str__(self):
        """ Print self"""
        print("House number: {}, Street Name: {}, Post Code: {},\
           province: {}, City: {}, Country: {}", house_number, street_name,  \
         post_code, province, city, country)
