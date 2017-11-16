# blog_app/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . models import Post

class BlogDeleteView(DeleteView):
  model = Post
  template_name = 'blog_app/post_delete.html'
  success_url = "/"

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog_app/post_edit.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_app/post_new.html'
    fields = '__all__'

class BlogListView(ListView):
    model = Post
    template_name = 'blog_app/post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    
   
