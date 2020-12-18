from django.shortcuts import render
from blog.models import Post
from .models import AboutUs , Services , Team , Testimony, Gallery, Application

# Create your views here.

def home(request):

    about = AboutUs.objects.all()
    services = Services.objects.all()
    team = Team.objects.all()
    testimony = Testimony.objects.all()
    gallery = Gallery.objects.all()
    application = Application.objects.all()
    posts = Post.objects.all().order_by('-created')
    latest_post = Post.objects.last()

    context = {  
        'about' : about ,
        'services' : services ,
        'team' : team ,
        'testimony' : testimony ,
        'gallery' : gallery ,
        'application' : application ,
        'posts' : posts ,
        'latest_post' : latest_post ,
    }

    return render(request , 'home/index.html' , context)