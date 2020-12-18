from .models import Category, Post , Comment

from django.contrib import admin

# Register your models here.



admin.site.register(Post )
class PostAdmin(admin.ModelAdmin):
        list_display=['title', 'publish']
        search_fields=['title', 'author']
        class Media:
            js=('tiny.js',)
        
admin.site.register(Category)
admin.site.register(Comment)


