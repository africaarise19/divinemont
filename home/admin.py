from django.contrib import admin

from .models import AboutUs , Services , Team , Testimony, Gallery, Application


    
admin.site.register(AboutUs )
class AboutUsAdmin(admin.ModelAdmin):
        list_display=['title', 'publish']
        search_fields=['title', 'author']
        class Media:
            js=('tiny.js',)

admin.site.register(Services )
class ServicesAdmin(admin.ModelAdmin):
        list_display=['title', 'publish']
        search_fields=['title', 'author']
        class Media:
            js=('tiny.js',)

admin.site.register(Team )
class TeamAdmin(admin.ModelAdmin):
        list_display=['title', 'publish']
        search_fields=['title', 'author']
        class Media:
            js=('tiny.js',)

admin.site.register(Testimony )
class TestimonyAdmin(admin.ModelAdmin):
        list_display=['title', 'publish']
        search_fields=['title', 'author']
        class Media:
            js=('tiny.js',)

admin.site.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
        list_display=['title', 'publish']
        search_fields=['title', 'author']
        class Media:
            js=('tiny.js',)

admin.site.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
        list_display=['title', 'publish']
        search_fields=['title', 'author']
        class Media:
            js=('tiny.js',)

