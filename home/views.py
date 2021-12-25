from django.shortcuts import render


# Create your views here
def index(request):
    """A view to return the index page"""

    try:
        request.session['my_language']
    except:        
        request.session['my_language'] = {'language': 'en'}

    return render(request, "home/index.html")
