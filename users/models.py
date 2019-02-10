"""
@author : Herbert Nguruwe

"""
from django.db import models

# Create your models here.
class Person(models.Model):
    """ Person class"""

    foo = "default"
    SEX = (('M', 'MALE'),('F','FEMALE'))
    # Personal Data 
    first_name = models.CharField(max_length=70, default=foo)
    second_name = models.CharField(max_length=70,default=foo)
    surname_name = models.CharField(max_length=70, default=foo)
    maiden_name = models.CharField(max_length=70, default=foo)
    sex = models.CharField(max_length=1, default="M") # usage of 0/1 or bool will reduce memory 
    date_of_birth = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField('date created', auto_created=True)
    academic_level = models.CharField(max_length=100, default=foo)
    profile = models.CharField(max_length=400, default=foo)

    # contact details
    work_number = models.IntegerField(blank=True, null=True)
    home_number = models.IntegerField(blank=True, null=True)
    cell_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40,default=foo)

    def __init__(self):
        user_id = 90
        first_name = "herbert" 
        surname_name = "Nguruwe"


#===============================================================
#   Student inherits from  users
#===============================================================

class Student(Person):
    """docstring for ClassName"""
    foo = "default"

    # Additional data 
    stud_id = models.CharField(max_length=20, default=foo)

    #intrests must be done with a single word in the list 
    #that we have to loop through the list
    intrests = models.CharField(max_length=500, default=foo)

    # next of Keen
    """
    Next of keen is not  partof the user object, used just as fields 
    but can be changed later to a model in te latest version.
    The next keen values are prefixed by proceeding n_ to show that 
    they are next of keen 
    """
    n_first_name = models.CharField(max_length=70, default=foo)
    n_surname_name = models.CharField(max_length=70, default=foo)
    n_email = models.CharField(max_length=70, default=foo)

    def __init__(self):
        super(Student, self).__init__()
        self.arg = arg


#===============================================================
#   Adminstrators inistitutional for inherits from  users
#   I Adminstrators are institutional adminstrators
#===============================================================

class I_Adminstrator(Person):
    """docstring for ClassName"""
    foo = "default"
    
    i_admin_id=models.CharField(max_length=20, default=foo)
    inst_id= models.CharField(max_length=20, default=foo)

    def __init__(self):
        super(I_Adminstrator, self).__init__()
        self.arg = arg
      

#===============================================================
#   System adminstrators inistitutional for inherits from  users
#.  S Adminstrators are system adminstrators
#===============================================================

class S_Adminstrator(Person):
    """docstring for ClassName"""
    foo = "default"

    s_admin_id=models.CharField(max_length=20, default=foo)
    inst_id= models.CharField(max_length=20, default=foo)

    def __init__(self):
        super(Student, self).__init__()
        self.arg = arg
      
    def __str__(self):
        """Return resonable name"""
        var_name = self.first_name + self.surname_name
        return var_name;

#=============================================================
#      Address to Store address of users and insittutions
#=============================================================

class Address(models.Model):
    """"""
    foo = "default"
    house_number = models.IntegerField()
    street_name = models.CharField(max_length=200, default=foo)
    post_code = models.CharField(max_length=70, default=foo)
    province = models.CharField(max_length=100, default=foo)
    city = models.CharField(max_length=100, default=foo)
    country = models.CharField(max_length=100, default=foo)

    def __str__(self):
        """"""
        var_name = self.house_number + self.street_name 

    def __str__(self):
        """ Print self"""
        print("House number: {}, Street Name: {}, Post Code: {},\
           province: {}, City: {}, Country: {}", house_number, street_name,  \
         post_code, province, city, country)
