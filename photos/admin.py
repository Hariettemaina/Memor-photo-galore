from django.contrib import admin
from . models import Image,Location,Categories
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=("categories",)


admin.site.register(Image,ImageAdmin)
admin.site.register(Categories)
admin.site.register(Location)