from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

#urlspatterns
#the included URLconf '<module 'blog.urls' from '/home/nengkya/blog_project/blog/urls.py'>' does not appear to have any patterns in it
#if you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import
urlpatterns = [

    path('', BlogListView.as_view(), name = 'home'), #home.html

    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),

    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),

    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name = 'post_edit'),

    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name = 'post_delete')

]
