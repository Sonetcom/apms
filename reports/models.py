from django.db import models

# Create your models here.

class Report(models.Model):
	"""docstring for Report"""
	def __init__(self, arg):
		super(Report, self).__init__()
		self.arg = arg
		