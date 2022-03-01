from json import dumps
from django.shortcuts import render
from django.http import HttpResponse
import os
from clis.settings import BASE_DIR
import sys
sys.path.append("..")

# Create your views here.

def renderHome(request) :
    context = {}
    images = os.listdir(os.path.join(BASE_DIR, 'static_cdn\img'))
    context['images'] = images
    context['first_image'] = images[0]



    dataJSON = dumps(context)
    return render(request, 'personal/home.html', {'dataJSON': dataJSON})


def renderAcademics(request) :
    context = {}
    return render(request, 'personal/academics.html', context)

def renderContact(request) :
    context = {}
    return render(request, 'personal/contact.html', context)

def renderHappenings(request) :
    context = {}
    return render(request, 'personal/happenings.html', context)

def renderLabs(request) :
    context = {}
    return render(request, 'personal/labs.html', context)

def renderOpportunities(request) :
    context = {}
    return render(request, 'personal/opportunities.html', context)

def renderPeople(request) :
    context = {}
    return render(request, 'personal/people.html', context)


def renderPlacements(request) :
    context = {}
    return render(request, 'personal/placements.html', context)

def renderResearch(request) :
    context = {}
    return render(request, 'personal/research.html', context)



def sendImages(request) :
    print(BASE_DIR)
    print(os.path.join(BASE_DIR, 'static_cdn\img'))
    images = os.listdir(os.path.join(BASE_DIR, 'static_cdn\img'))
    for image in images :
        print(image)
    return HttpResponse("Hello")