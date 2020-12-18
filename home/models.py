from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    number = models.IntegerField()

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'

    def __str__(self):
        return self.title


class Services(models.Model):
    heading = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='services/')


    class Meta:
        verbose_name = 'services'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')


    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team'

    def __str__(self):
        return self.name

class Testimony(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='testimony/')


    class Meta:
        verbose_name = 'testimony'
        verbose_name_plural = 'testimonials'

    def __str__(self):
        return self.name

class Gallery(models.Model): 
    description = models.CharField(max_length=100)
    image_gallery = models.ImageField(upload_to='gallery/')


    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'

    def __str__(self):
        return self.description

class Application(models.Model): 
    description = models.CharField(max_length=100)
    application_form = models.FileField(upload_to='Application', blank=True)


    class Meta:
        verbose_name = 'Application form'
        verbose_name_plural = 'Application forms'

    def __str__(self):
        return self.description

    
