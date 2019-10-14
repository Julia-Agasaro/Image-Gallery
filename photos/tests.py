from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali = Location(location = 'Kigali')
        self.kigali.save_location()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
   
   
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))

    # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location='Kigali')
        self.location.save()

        self.category = Category(category_name='Chocolates')
        self.category.save()

        self.image_test = Image(description='All Time Fave',location=self.location,category=self.category)
        self.image_test.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test,Image))


    