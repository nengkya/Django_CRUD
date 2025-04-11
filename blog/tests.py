from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse


#create your tests here
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username = 'testuser', email = 'test@email.com', password = 'secret')

        self.post = Post.objects.create(title = 'KCIC', body = 'Kereta Cepat Indonesia China', author = self.user)


    def test_string_representation(self):
        post = Post(title = 'A sample title')
        self.assertEqual(str(post), post.title)


    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'KCIC')


    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_post_detail_view(self):
        #response = self.client.get('/post/1') AssertionError: 301 != 200
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)


    def test_pos_create_view(self):
        response = self.client.post(reverse('post_new'), {'title' : 'Test new title', 'body' : 'New test body text', 'author' : self.user})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test new title')


    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args = '1'), {'title' : 'Updated title', 'body' : 'Updated body text'})
        self.assertEqual(response.status_code, 302)


    def test_post_delete_view(self):
        #response = self.client.get(reverse('post_delete', args = '2'))
        #AssertionError: 404 != 200        
        response = self.client.get(reverse('post_delete', args = '1'))
        self.assertEqual(response.status_code, 200)
