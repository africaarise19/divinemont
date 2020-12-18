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


admin.site.site_header = "Africa Arise AdminPanel"
admin.site.site_title = "Africa Arise App Admin"
admin.site.site_index_title = "Welcome To Africa Arise Admin Panel"

