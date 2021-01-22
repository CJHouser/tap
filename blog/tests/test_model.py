from django.test import TestCase
from blog.models import BlogPost 
from django.utils import timezone

class ModelTest(TestCase):
    def test_create(self):
        bp = BlogPost.objects.create(title="test_create"
            , creation_date=timezone.now()
            , content="test_create")
        self.assertTrue(isinstance(bp, BlogPost))
        self.assertEqual(bp.__str__(), bp.title)

# References:
# https://stackoverflow.com/questions/51148893/object-created-even-if-field-was-required
