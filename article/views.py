from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article

class ArticleDetail(DetailView):
    model = Article

class ArticleList(ListView):
    model = Article

    
