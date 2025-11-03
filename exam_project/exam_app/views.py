from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def films(request):
    films = {
        'Joker': 7.5,
        'Inception': 8.8,
        'Titanic': 7.9,
        'Interstellar': 8.6
    }
    return render(request, 'films.html', {'films': films})