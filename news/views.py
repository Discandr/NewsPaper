#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post

from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'newses.html'
    context_object_name = 'newses'
    queryset = Post.objects.order_by('-id')
    paginate_by = 3



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsid.html'
    context_object_name = 'newsid'


class NewsFiltered(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = ['-post_time']
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class NewsAdd(CreateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm
    success_url = '/news/'


class NewsEdit(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    form_class = PostForm
    success_url = '/news/<int:pk>/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



class NewsDelete(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'




class PostDetail(DetailView):
    template_name = 'details.html'
    queryset = Post.objects.all()
    success_url = '/news/<int:pk>/'



