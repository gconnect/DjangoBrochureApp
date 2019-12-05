from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.utils import timezone

from .models import Blog


class IndexView(generic.ListView):
    template_name = 'brochure/index.html'
    context_object_name = 'latest_blog_list'
    def get_queryset(self):
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'brochure/detail.html'
