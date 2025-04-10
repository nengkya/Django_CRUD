from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView

#create your views here
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__' #using ModelFormMixin (base class of BlogCreateView) without the 'fields' attribute is prohibited

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body'] #using ModelFormMixin (base class of BlogUpdateView) without the 'fields' attribute is prohibited


