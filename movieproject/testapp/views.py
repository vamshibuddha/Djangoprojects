from django.shortcuts import render
from testapp.forms import movieform
from testapp.models import moviemodel

# Create your views here.
def index_view(request):
    return render(request, 'testapp/home.html')

def addmovie_view(request):
    form = movieform()
    if request.method=='POST':
        form=movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request, 'testapp/addmovie.html', {'form':form})

def listmovie_view(request):
    movie_list = moviemodel.objects.all()
    return render(request, 'testapp/listmovies.html', {'movie_list': movie_list})
