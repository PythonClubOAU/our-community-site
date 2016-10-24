from django.shortcuts import render


def index(request):
    return render(request, 'ClubPython/blog/index.html')