from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Extra
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants
    })


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


class PlantCreate(CreateView):
    model = Plant
    fields = ['givenName', 'plantName', 'description', 'potSize', 'height']


class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'


class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'


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

# request post . date
# get exisiting string, spit on dash - reverse - put it back together


class ExtraList(ListView):
    model = Extra


class ExtraDetail(DetailView):
    model = Extra


class ExtraCreate(CreateView):
    model = Extra
    fields = '__all__'


class ExtraUpdate(UpdateView):
    model = Extra
    fields = ['name', 'description']


class ExtraDelete(DeleteView):
    model = Extra
    success_url = '/extras'


def assoc_extra(request, plant_id, extra_id):
    Plant.objects.get(id=plant_id).extras.add(extra_id)
    return redirect('detail', plant_id=plant_id)


def disassoc_extra(request, plant_id, extra_id):
    Plant.objects.get(id=plant_id).extras.remove(extra_id)
    return redirect('detail', plant_id=plant_id)
