from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'brochure/index.html'

    def get_queryset(self):
        return HttpResponse("hello world")