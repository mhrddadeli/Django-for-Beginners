from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Post = Post.objects.create(text="salam test case!")
        
    def test_model_content(self):
        self.assertEqual(self.Post.text, "salam test case!")

    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)
        
    def test_hompage(self):
        responce = self.client.get(reverse("home"))
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, "home.html")
        self.assertContains(responce, "salam test case!")
