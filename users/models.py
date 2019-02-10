from django.db import models

# Create your models here.
class Person(models.Model):
    """ Person class"""

    # Personal Data 
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70)
    surname_name = models.CharField(max_length=70)
    maiden_name = models.CharField(max_length=70)
    sex = models.CharField()
    date_of_birth = models.DateTimeField()
    create_date = models.DateTimeField('date created', auto_created=True)
    academic_level = models.CharField(max_length=100)
    profile = models.CharField(max_length=400)

    # contact details
    work_number = models.IntegerField()
    home_number = models.IntegerField()
    cell_number = models.IntegerField()
    email = models.CharField()

    def __init__(self):


#===============================================================
#   Student inherits from  users
#===============================================================
class Student(Person):
    """docstring for ClassName"""

    # Additional data 
    stud_id = models.CharField()

    #intrests must be done with a single word in the list 
    #that we have to loop through the list
    intrests = models.CharField(max_length=500)

    # next of Keen
    """
    Next of keen is not  partof the user object, used just as fields 
    but can be changed later to a model in te latest version.
    The next keen values are prefixed by proceeding n_ to show that 
    they are next of keen 
    """
    n_first_name = models.CharField(max_length=70)
    n_surname_name = models.CharField(max_length=70)
    n_email = models.CharField()

    def __init__(self):
        super(Student, self).__init__()
        self.arg = arg


#===============================================================
#   Adminstrators inistitutional for inherits from  users
#   I Adminstrators are institutional adminstrators
#===============================================================
class I_Adminstrator(Person):
    """docstring for ClassName"""
    
    admin_id=models.CharField()
    inst_id= models.CharField()

    def __init__(self):
        super(I_Adminstrator, self).__init__()
        self.arg = arg
      

#===============================================================
#   System adminstrators inistitutional for inherits from  users
#.  S Adminstrators are system adminstrators
#===============================================================
class S_Adminstrator(Person):
    """docstring for ClassName"""
    def __init__(self):
        super(Student, self).__init__()
        self.arg = arg
      
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
