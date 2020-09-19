<<<<<<< HEAD
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rooms.models import Room



def list_rooms(request):
    
    data = serializers.serialize("json", Room.objects.all())
    response = HttpResponse(content=data)
    return response
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> cc2656b759cba23d39d51007debe9d5b6390a042
