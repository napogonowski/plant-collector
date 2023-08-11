from django.shortcuts import render


plants = [
    {'name': 'Croton Petra', 'type': 'Shurb', 'description': 'leathery foliage that is vivid shades of green yellow red and orange and changes depending on the season and light conditions.', 'height': '150'},
    {'name': 'Happy Plant', 'type': 'Strappy Leaf', 'description': 'shade plant with bright green-yellow variegated foliage and a rosette habit.', 'height': '200'},
]

# Create your views here.
def home (request): 
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def plants_index (request):
    return render(request, 'plants/index.html', {
        'plants': plants
    })