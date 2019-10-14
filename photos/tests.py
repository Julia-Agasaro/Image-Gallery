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


    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.image_test.save_image()
        self.image_test.delete_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id,'collection/test_one.jpg')
        changed_img = Image.objects.filter(image='collection/test_one.jpg')
        self.assertTrue(len(changed_img)>0)

    
    def test_search_by_image(self):
        category = 'Chocolates'
        found_img = self.image_test.search_by_image(category)
        self.assertTrue(len(found_img)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='Chocolates')
        self.category.save()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_update_category(self):
        new_category_name = 'Babies'
        self.category.update_category(self.category.id,new_category_name)
        changed_category = Category.objects.filter(category_name='Food')
        self.assertTrue(len(changed_category)>0)

    

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)