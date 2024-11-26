from django.shortcuts import render, HttpResponse
from django.db import models


# Create your views here.
def Agent(request):
    # name = models.CharField(max_length=100)
    return HttpResponse("Agent")


def Campaign(request):
    # name = models.CharField(max_length=100)
    return HttpResponse("Campaign")


def CampaignResults(request):
    # name = models.CharField(max_length=100)
    return HttpResponse("Campaign Results")
