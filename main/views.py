from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import  DishCategory, Dish, EventsCategory, Chefs, Gallery
from .forms import ReservationForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test


class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        events = EventsCategory.objects.filter(is_visible=True)
        chefs = Chefs.objects.all()
        gallery = Gallery.objects.all()
        form = ReservationForm()

        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_gallery'] = 'Check <span>Our Gallery</span>'
        context['categories'] = categories
        context['events'] = events
        context['chefs'] = chefs
        context['gallery'] = gallery
        context['form'] = form

        return context

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше бронювання прийнято!')
            return redirect('index')



# Create your views here.
#def index(request):
    #if request.method == 'POST':
        #form = ReservationForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return HttpResponse('Дякуемо за ваше бронювання! Ми зв\'яжемося з вами найближчім часом!')
    #if request.method == 'GET':
        #categories = DishCategory.objects.filter(is_visible=True)
        #events = EventsCategory.objects.filter(is_visible=True)
        #chefs = Chefs.objects.all()
        #gallery = Gallery.objects.all()
        #form = ReservationForm()

        #context = {
            #'title_menu': 'Check Our <span>Yummy Menu</span>',
            #'title_gallery': 'Check <span>Our Gallery</span>',
            #'categories': categories,
            #'events': events,
            #'chefs': chefs,
            #'gallery': gallery,
            #'form': form,
        #}
        #return render(request, 'main.html', context=context)



#def index1(request):
    #categories = EventsCategory.objects.filter(is_visible=True)
    #return HttpResponse('\n'.join(map(str, categories)))
    #return render(request, 'main.html')


#def index2(request):
    #return HttpResponse('\n'.join(map(str, Chefs.objects.all())))
    #return render(request, 'main.html')


#def index3(request):
    ##return HttpResponse('\n'.join(map(str, Gallery.objects.all())))
    #return render(request, 'main.html')

def manager(request):
    ...
