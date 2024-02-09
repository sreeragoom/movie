from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from movie_app.forms import MovieForm
from movie_app.models import Movies, Category


# Create your views here.
# def index(request):
#     movies = Movies.objects.all()
#     categories = Category.objects.all()
#     items_by_category = {}
#
#     for category in categories:
#         items_by_category[category] = Movies.objects.filter(category=category)
#     return render(request, 'menu.html', {'movie': movies,'items_by_category': items_by_category})
#
#
def detail(request, id):
    movie = Movies.objects.get(id=id)
    return render(request, 'about.html', {'movies': movie})


# views.py





def index(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies=Movies.objects.all().filter(category=c_page,)
    else:
        movies=Movies.objects.all().filter()

    return render(request,'menu.html',{'category':c_page,'movies': movies})
@login_required
def update(request, id):
    movie = get_object_or_404(Movies, id=id)

    # Check if the current user is the one who added the movie
    if request.user != movie.user:
        # Handle unauthorized access, such as redirecting to a 403 page
        return render(request, 'unauthorized_access.html')

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/', category_slug=movie.category.slug, movie_slug=movie.slug)  # Redirect to movie detail page
    else:
        form = MovieForm(instance=movie)

    return render(request, 'update.html', {'form': form, 'movie': movie})


@login_required
def delete(request, id):
    movie = get_object_or_404(Movies, id=id)

    if request.user != movie.user:
        return render(request, 'unauthorized_access del.html')

    if request.method == 'POST':
        movie.delete()
        return redirect('/')

    return render(request, 'delete.html', {'movie': movie})



def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            ()
            # Check if 'poster' key exists in the request.FILES dictionary
            if 'poster' in request.FILES:

                form.save()
                return HttpResponseRedirect('/')  # Redirect to success page

            else:
                form.add_error('poster', 'Poster is required.')
            form.save()

        else:
            redirect('movie_app:add')
    else:
        form = MovieForm()

    return render(request, 'add.html', {'form': form})
