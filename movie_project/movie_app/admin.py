from django.contrib import admin

# Register your models here.
from  . models import Category,Movies


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title','year']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Movies,MoviesAdmin)