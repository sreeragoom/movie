from django.shortcuts import render, redirect
from movie_app.models import Movies,Category
from django.db.models import Q



# Create your views here.

def searchResult(request):
    movie=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movie=Movies.objects.all().filter(Q(slug__icontains=query) | Q(description__icontains=query))
        return render(request,'search.html',{'query':query,'movies':movie})
