from django.shortcuts import render
from .models import Blog 

# Create your views here.
def index(request):
	blogs = Blog.objects
	return render(request, 'index.html', {'blogs': blogs})

def about(request):
	blogs = Blog.objects
	return render(request, 'about.html', {'blogs': blogs})

def contact(request):
	blogs = Blog.objects
	return render(request, 'contact.html', {'blogs': blogs})
