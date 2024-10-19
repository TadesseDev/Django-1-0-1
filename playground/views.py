from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def root(request):
  return HttpResponse("Root app")
def say_hello(request):
  return HttpResponse("hello world form the")
