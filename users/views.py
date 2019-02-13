from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index from user')

def create(request):
    return HttpResponse("Hello from Create")


def create_student():
	pass