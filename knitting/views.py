from django.shortcuts import render
from django.http import HttpResponse
from knitting.models import Student, Course
from knitting.forms import RegisterForm
from django.utils import timezone
import datetime
def index(request):

    upcoming_courses=Course.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
    context_dict={'categories': upcoming_courses}
    return render(request, '/Documents/Django/fabric/templates/knitting/index.html',context_dict)

def about(request):
    return render(request, '/Documents/Django/fabric/templates/knitting/about.html',{})

def registered(request):
    #odpowiedz na poprawne zarejestrowanie sie
    return HttpResponse('Thanks for registration </br> powrot do strony glownej </br> <a href="http://127.0.0.1:8000/">powrot</a>')
def notregistered(request):
    #odpowiedz gdy wystapil blad w rejestracji:
    return HttpResponse('Registration collapsed please return to registration form <a href="http://127.0.0.1:8000/registration/">rejestracja</a>')


def register_view(request):
    #glowny watek rejestracji
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return registered(request)
        else:
            return notregistered(request)
    else:
        form=RegisterForm()
    return  render(request, '/Documents/Django/fabric/templates/knitting/registration.html', {'form':form})