from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'kfc/index.html')


@login_required
def home(request):
    return render(request, 'kfc/home.html')
