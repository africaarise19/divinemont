from django.contrib import admin

from .models import AboutUs , Services , Team , Testimony


    
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


