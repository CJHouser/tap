from django.test import TestCase
from blog.models import BlogPost 
from django.utils import timezone

from django.urls import reverse

class ViewTest(TestCase):
    def test_blog_index(self):
        bp = BlogPost.objects.create(
            title="test_blog_index_title_field",
            created_at=timezone.now(),
            content="test_blog_index_content_field"
        )
        url = reverse("blog:index")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, bp.title)
        self.assertContains(
            resp,
            bp.created_at.strftime("%Y-%m-%d %H:%M %Z")
        )
        self.assertNotContains(resp, bp.content)

    def test_post_detail(self):
        bp = BlogPost.objects.create(
            title="test_post_detail:title",
            created_at=timezone.now(),
            content="test_post_detail:content"
        )
        url = reverse("blog:detail", args=(bp.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, bp.title)
        self.assertContains(
            resp,
            bp.created_at.strftime("%Y-%m-%d %H:%M %Z")
        )
        self.assertContains(resp, bp.content)
