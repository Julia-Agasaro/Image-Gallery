from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def photos(request):
    date = dt.date.today()
    photo = Image.photos()
    return render(request, 'photos.html', {"date": date,"image": photo})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})