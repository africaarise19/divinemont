from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('' , include('home.urls' , namespace='home')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Divine Montessori AdminPanel"
admin.site.site_title = "Divine Montessori App Admin"
admin.site.site_index_title = "Welcome To Divine Montessori Admin Panel"

