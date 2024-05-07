from django.shortcuts import render
from django.http import HttpResponse
from .models import  DishCategory, EventsCategory, Chefs, Gallery


# Create your views here.
def index(request):
    #categories = DishCategory.objects.filter(is_visible=True)
    #for item in categories:
    #    for dish in item.dish_set.filter(is_visible=True):
    #        dish.category = item
    #return HttpResponse('\n'.join(map(str, categories)))
    return render(request, 'main.html')


def index1(request):
    #categories = EventsCategory.objects.filter(is_visible=True)
    #return HttpResponse('\n'.join(map(str, categories)))
    return render(request, 'main.html')


def index2(request):
    #return HttpResponse('\n'.join(map(str, Chefs.objects.all())))
    return render(request, 'main.html')


def index3(request):
    #return HttpResponse('\n'.join(map(str, Gallery.objects.all())))
    return render(request, 'main.html')


