from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'new_blog.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model= Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')