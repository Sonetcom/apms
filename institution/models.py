# -*- coding: utf-8 -*-
"""
Institution class, contains the attributes and names of the class.
"""
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Institution(models.Model):
    """
    This institution class, contains the attributes and names of the class
    """
    #inst_name = models.CharField(max_length=200, help="Name of the institution")
    #inst_place = models.CharField(max_length=200, help="Area of the instution")
    inst_num = models.CharField(max_length=10)

    class Meta:
        """ Order by the institutional Number."""
        ordering = ['inst_num']

    def __str__(self):
        """ This method is used when we want to print the name of the institution. """
        #return self.inst_name
        pass

    def get_absolute_url(self):
        """ The representing the model."""
        return reverse("model_detail", args=[str(self.inst_num)])

    @property
    def get_address(self):
        """ Get the address of the intsitution. """
        pass

    @property
    def get_admin(self):
        """Get the admin of the institution."""
        pass
