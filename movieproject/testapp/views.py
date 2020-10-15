from django.shortcuts import render
from testapp.forms import movieform
from testapp.models import moviemodel

# Create your views here.
def index_view(request):
    return render(request, 'testapp/home.html')

def addmovie_view(request):
    form = movieform()
    return render(request, 'testapp/addmovie.html', {'form':form})

