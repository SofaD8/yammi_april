from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import  DishCategory, Dish, EventsCategory, Chefs, Gallery
from .forms import ReservationForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


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
        context['title_events'] = 'Share <span>Your Moments</span> In Our Restaurant'
        context['title_chefs'] = 'Our <span>Proffesional</span> Chefs'
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


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def manager(request):
    return HttpResponse('Manager page')
