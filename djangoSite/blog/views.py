from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hey response.")


def post(request):
    return HttpResponse("simple post")
