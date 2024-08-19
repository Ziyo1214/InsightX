from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'visit/main.html', {'title': 'Insight X'})

def video(request):
    return render(request, 'visit/video.html', {'title': 'Insight X'})

def faq(request):
    return render(request, 'visit/faq.html', {'title': 'Insight X'})

def blog(request):
    return render(request, 'visit/blog.html', {'title': 'Insight X'})

def opinions(request):
    return render(request, 'visit/opinions.html', {'title': 'Insight X'})
def elevator(request):
    return render(request, 'visit/elevator.html', {'title': 'Insight X'})



def login(request):
    return render(request, 'visit/login.html', {'title': 'Insight X'})


def adminmain(request):
    return render(request, 'admin/main.html', {'title': 'Insight X'})
