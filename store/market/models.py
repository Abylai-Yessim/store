from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=False)
    image_url = models.URLField(null=True, blank=True) 
    
    def __str__(self) -> str:
        return self.title

class Busket(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=False)
    image_url = models.URLField(null=True, blank=True) 

class Fields(models.Model):
    user_id = models.IntegerField(max_length=50)
    blog_id = models.IntegerField()
    

    class Meta:
        verbose_name = 'Fields'
        verbose_name_plural = 'Fields'

