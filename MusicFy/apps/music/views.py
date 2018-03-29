from django.shortcuts import render, HttpResponse, redirect
from ..login.models import User

# Create your views here.
def index(request, id):
    if request.session.get('id') == None:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user
    }
    return render(request, 'music/homepage.html', context)