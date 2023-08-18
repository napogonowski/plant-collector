from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plant, Extra
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def plants_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {
        'plants': plants
    })


@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    # create list of extras id the plant does have
    id_list = plant.extras.all().values_list('id')
    extras_plant_doesnt_have = Extra.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'plants/detail.html', {
        'plant': plant,
        'feeding_form': feeding_form,
        'extras': extras_plant_doesnt_have
    })


class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['givenName', 'plantName', 'description', 'potSize', 'height']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = '__all__'


class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants'


@login_required
def add_feeding(request, plant_id):
    print("Roads ?")
    form = FeedingForm(request.POST)
    print("Where we're going ...")
    if form.is_valid():
        print("we dont need roads ")
        new_feeding = form.save(commit=False)
        new_feeding.plant_id = plant_id
        new_feeding.save()
    print(form.errors)
    return redirect('detail', plant_id=plant_id)


class ExtraList(LoginRequiredMixin, ListView):
    model = Extra


class ExtraDetail(LoginRequiredMixin, DetailView):
    model = Extra


class ExtraCreate(LoginRequiredMixin, CreateView):
    model = Extra
    fields = '__all__'


class ExtraUpdate(LoginRequiredMixin, UpdateView):
    model = Extra
    fields = ['name', 'description']


class ExtraDelete(LoginRequiredMixin, DeleteView):
    model = Extra
    success_url = '/extras'


@login_required
def assoc_extra(request, plant_id, extra_id):
    Plant.objects.get(id=plant_id).extras.add(extra_id)
    return redirect('detail', plant_id=plant_id)


@login_required
def disassoc_extra(request, plant_id, extra_id):
    Plant.objects.get(id=plant_id).extras.remove(extra_id)
    return redirect('detail', plant_id=plant_id)


def signup(request):
    error_message = ''
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - please try again'
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)
