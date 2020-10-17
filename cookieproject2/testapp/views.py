from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testapp/name.html')

def age_view(request):
    name = request.GET['name']
    response = render(request, 'testapp/age.html')
    response.set_cookie('name', name)
    return response

def girlfrnd_view(request):
    age = request.GET['age']
    response = render(request, 'testapp/girlfrnd.html')
    response.set_cookie('age', age)
    return response

def results_view(request):
    gfname= request.GET['girlfrnd']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    response = render(request, 'testapp/results.html', {'name': name, 'age': age, 'gfname': gfname})
    return response