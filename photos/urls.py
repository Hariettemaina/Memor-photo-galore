from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.gallery,name = 'gallery'),
    re_path(r'^location/(\d+)',views.location,name = 'location'),
    re_path(r'^search/',views.search,name='search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




# urlpatterns = [
#     path('', views.gallery, name='gallery'),
#     path('photo/<str:pk>/', views.viewPhoto, name='photo'),
#     path('add/', views.addPhoto, name='add')
# ]