from django.shortcuts import render
from .models import Image,Location,Categories

# Create your views here.
def gallery(request):
    images = Image.all_images()
    locations = Location.objects.all()
    return render(request, 'photos/index.html', {"images":images,"locations":locations})

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    return render(request, 'photos/location.html', {"location":selected_location,"locations":locations,"images":images})

def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        return render(request,'photos/search.html',{"images":searched_images,"category":search_term})






# from django.shortcuts import render

# # Create your views here.

# def gallery(request):
#     return render(request, 'photos/gallery.html')

# def viewPhoto(request, pk):
#     return render(request, 'photos/photo.html')

# def addPhoto(request):
#     return render(request, 'photos/add.html')

