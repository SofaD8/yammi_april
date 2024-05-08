from django.shortcuts import render
from django.http import HttpResponse
from .models import  DishCategory, Dish, EventsCategory, Chefs, Gallery


# Create your views here.
def index(request):
    categories = DishCategory.objects.filter(is_visible=True)
    #gallery = Gallery.objects.all()
    #for item in categories:
    #    for dish in item.dishes.filter(is_visible=True):
    #        dish.category = item
    #return HttpResponse('\n'.join(map(str, categories)))
    context = {
        'title_menu': 'Check Our <span>Yummy Menu</span>',
        'title_gallery': 'Check <span>Our Gallery</span>',
        'categories': categories,
        #'gallery': gallery,
    }
    return render(request, 'main.html')


def index1(request):
    #categories = EventsCategory.objects.filter(is_visible=True)
    #return HttpResponse('\n'.join(map(str, categories)))
    return render(request, 'main.html')


def index2(request):
    #return HttpResponse('\n'.join(map(str, Chefs.objects.all())))
    return render(request, 'main.html')


def index3(request):
    ##return HttpResponse('\n'.join(map(str, Gallery.objects.all())))
    return render(request, 'main.html')

def manager(request):
    ...
