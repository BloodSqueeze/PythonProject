from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if request.session.get('id') == None:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user
    }
    return render(request, 'music/homepage.html', context)