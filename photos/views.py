from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'photos/gallery.html')

def viewPhoto(request):
    return render(request, 'photos/photo.html')

def gallery(request):
    return render(request, 'photos/gallery.html')

