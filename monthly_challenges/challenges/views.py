from modulefinder import ReplacePackage
from django.http import HttpResponse, HttpResponseNotFound, response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def month_challenge(req,month):
    # options=['January', 'February', 'March', 'April', 'May', 
    #          'June', 'July', 'August', 'September', 
    #          'October', 'November','December']
    Response=None
    if month=='January':
        Response="Eat no meat for the entire month"
    
    elif month=='February':
        Response="walk for at least 20 minutes every day!"
    
    elif month=='March':
        Response='Learn django for at lest 20 minutes every day!'
    
    else:
        return HttpResponseNotFound("this month is not supported!")
    return HttpResponse(Response)