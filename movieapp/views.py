
from django.shortcuts import redirect, render
from .models import Movies
# Create your views here.
def index(request):

    dict_movies = {
        'movie': Movies.objects.all()
    }
    return render(request, 'index.html', dict_movies)

def details(request, id):
    dict_movies = {
        'movie': Movies.objects.get(id=id)
    }
    return render(request,'details.html', dict_movies)

def add(request):
    return render(request, 'add.html')

def update(request,id):
    dict_movie = {
        'movie':Movies.objects.get(id=id)
    }
    return render(request, 'update.html', dict_movie)

def addmovie(request):
    if request.method == 'POST':
        name = request.POST['name']
        des = request.POST['des']
        year = request.POST['year']
        image = request.FILES['image']

        movie = Movies(
            movie_name = name,
            movie_des = des,
            movie_year = year,
            movie_image = image
        )
        movie.save()
        print("inserted successfully")
        return redirect('/')
    return render(request, 'add.html')

def updatemovie(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        des = request.POST['des']
        year = request.POST['year']
        image = request.FILES['image']

        movie = Movies.objects.get(id=id)
        movie.movie_name = name
        movie.movie_des = des
        movie.movie_year = year
        movie.movie_image = image
        
        movie.save()
        print("Updated successfully")
        return redirect('/')

def delete(request,id):
    movie = Movies.objects.get(id=id)
    movie.delete()
    return redirect('/')