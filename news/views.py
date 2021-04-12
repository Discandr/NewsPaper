#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'newses.html'
    context_object_name = 'newses'
    queryset = Post.objects.order_by('-id')
#    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'newsid.html'
    context_object_name = 'newsid'
