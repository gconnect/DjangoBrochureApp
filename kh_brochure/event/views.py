from django.shortcuts import render
from django.views import generic
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'brcochure/index.html'
