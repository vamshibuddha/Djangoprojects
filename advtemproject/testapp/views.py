from django.shortcuts import render

# Create your views here.
def news_view(request):
    return render(request, 'testapp/home.html')

def movies_view(request):
    return render(request, 'testapp/movies.html')
def sports_view(request):
    return render(request, 'testapp/sports.html')
def politics_view(request):
    return render(request, 'testapp/politics.html')