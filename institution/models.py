# -*- coding: utf-8 -*-
"""
Institution class, contains the attributes and names of the class.
"""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from django.urls import reverse

class Institution(models.Model):
    """
    This institution class, contains the attributes and names of the class
    """
    #inst_name = models.CharField(max_length=200, help="Name of the institution")
    #inst_place = models.CharField(max_length=200, help="Area of the instution")
    inst_id = models.CharField(max_length=10, default="CPTUCT")
    inst_name = models.CharField(max_length=200, default="Herentals college")
    inst_abbr = models.CharField(max_length=10, default="HC")

    class Meta:
        """ Order by the institutional Number."""
        ordering = ['inst_id']

    def __str__(self):
        """ This method is used when we want to print the name of the institution. """
        #return self.inst_name
        pass

    def __eq__(self, other):
        """
        """
        return self.inst_id == other.inst_id

    def get_absolute_url(self):
        """ The representing the model."""
        return reverse("model_detail", args=[str(self.inst_id)])

    @property
    def get_address(self):
        """ Get the address of the intsitution. """
        pass

    @property
    def get_admin(self):
        """Get the admin of the institution."""
        pass
