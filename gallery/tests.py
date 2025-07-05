from django.test import TestCase
from django.core.files import File 
from .models import Image


# Create your tests here.

class GalleryModelTest(TestCase):

    def test_gallery_model_save_and_retrieve(self):
        image_1 = Image(
            title = 'image 1',
            image = File(open('gallery/test_images/test_image_1.png', 'rb'))

        )
        image_1.save()

        image_2 = Image(
            title = 'artimageicle 2',
            image = File(open('gallery/test_images/test_image_2.png', 'rb'))
        )

        image_2.save()

        all_images = Image.objects.all()

        self.assertEqual(len(all_images), 2)

        self.assertEqual(
            all_images[0].title,
            image_1.title
        )
        self.assertEqual(
            all_images[0].image,
            image_1.image
        )


        self.assertEqual(
            all_images[1].title,
            image_2.title
        )
        self.assertEqual(
            all_images[1].image,
            image_2.image
        )
        