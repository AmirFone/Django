from modulefinder import ReplacePackage
from django.http import HttpResponse, HttpResponseNotFound, response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
options={'January':"Eat no meat for the entire month", 
         'February':"walk for at least 20 minutes every day!", 
         'March':'Learn django for at lest 20 minutes every day!', 
         'April':"Eat no meat for the entire month", 
         'May':"walk for at least 20 minutes every day!", 
         'June':'Learn django for at lest 20 minutes every day!', 
         'July':"Eat no meat for the entire month",
         'August':"walk for at least 20 minutes every day!",
         'September':'Learn django for at lest 20 minutes every day!', 
         'October':"Eat no meat for the entire month",
         'November':"walk for at least 20 minutes every day!",
         'December':'Learn django for at lest 20 minutes every day!'}

def month_challenge(req,month):
    if month in options:
        return HttpResponse(options[month])
    else:
        return HttpResponseNotFound("this month is not supported!")