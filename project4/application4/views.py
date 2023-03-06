from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def santhosh(request):
    return HttpResponse("<marquee><h1>SANTHOSH IS WORST FELLOW</h1></marquee>")

def santu(request):
    return HttpResponse("<marquee><h1>SANTU IS THE BEST</h1></marquee>")

def ramram(request):
    return HttpResponse("<h1>RAM RAM SATYAHEII</h1>")
