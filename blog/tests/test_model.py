# Reference:
# https://alcher.dev/2020/what-to-test-in-django-models/

from django.test import TestCase
from blog.models import BlogPost 
from django.utils import timezone
from datetime import datetime

class BlogPostModelTest(TestCase):
    def setUp(self):
        self.blogpost = BlogPost.objects.create(
            title="test_create:title",
            content="test_create:content"
        )

    # Field tests
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.blogpost.title, str)
        self.assertIsInstance(self.blogpost.content, str)

    def test_it_has_timestamps(self):
        self.assertIsInstance(self.blogpost.created_at, datetime)
        self.assertIsInstance(self.blogpost.modified_at, datetime)

    # Field tests
    def test_title_updates(self):
        old = self.blogpost.title
        new = "test_title_updates:title"
        self.blogpost.title = new
        self.blogpost.save()
        self.assertNotEqual(old, self.blogpost.title)
        self.assertEqual(new, self.blogpost.title)

    def test_content_updates(self):
        old = self.blogpost.content
        new = "test_content_updates:content"
        self.blogpost.content = new
        self.blogpost.save()
        self.assertNotEqual(old, self.blogpost.content)
        self.assertEqual(new, self.blogpost.content)

    # Method tests
    def test_timestamps_equal_on_creation(self):
        # save() if conditional is true
        self.assertEqual(self.blogpost.created_at, self.blogpost.modified_at)

    def test_string_representation_is_title(self):
        # __str__
        self.assertEqual(str(self.blogpost), self.blogpost.title)

    def test_created_at_unchanged_on_modification(self):
        # save() if conditional is false
        before_change_created_at = self.blogpost.created_at
        self.blogpost.title = "diff"
        self.blogpost.save()
        self.assertEqual(self.blogpost.created_at, before_change_created_at)

    def test_modified_at_changed_on_modification(self):
        # save() updates modified_at
        before_change_modified_at = self.blogpost.modified_at
        self.blogpost.title = "not_the_same"
        self.blogpost.save()
        self.assertTrue(before_change_modified_at < self.blogpost.modified_at)

