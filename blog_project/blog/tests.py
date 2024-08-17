from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from.models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="testuser", email="test@gmail.com", password="secret"
        )
        
        cls.post = Post.objects.create(
            title="title", body="body", author=cls.user,
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.title, "title")
        self.assertEqual(self.post.body, "body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
        
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'body')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/10000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, 'post_detail.html')
        
    def test_post_createview(self):
        response = self.client.post(
            reverse("post_create"),
            {
                'title': "New Title",
                'body': "New Body",
                'author': self.user.id,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New Title")
        self.assertEqual(Post.objects.last().body, "New Body")
    
    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_update", args="1"),
            {
                'title': "Updated Title",
                'body': "Updated Body"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated Title")
        self.assertEqual(Post.objects.last().body, "Updated Body")
    
    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
        
        
                
