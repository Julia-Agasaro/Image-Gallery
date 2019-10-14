from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):

    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

class Category(models.Model):
    
    category_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

       
class Image(models.Model):
    image=models.ImageField(upload_to='picture/')
    name = models.CharField(max_length=40)
    description=models.TextField()
    location=models.ForeignKey(Location, db_column='location_name', blank=True)
    category = models.ForeignKey(Category,db_column='category_name', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
   
   
    @classmethod
    def photos(cls):
        today = dt.date.today()
        photos = cls.objects.all()
        return photos

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod  
    def search_by_image(cls,search_term):
        image = cls.objects.filter(category__category_name__contains=search_term)
        return image


    @classmethod
    def filter_by_location(cls, location):
        image = cls.objects.filter(location=location)
        return image
    
    @classmethod
    def filter_by_category(cls, category):
        image = cls.objects.filter(category=category)
        return image