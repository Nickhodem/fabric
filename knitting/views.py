from django.shortcuts import render
from django.http import HttpResponse
from knitting.models import Student, Course, Tutor
from knitting.forms import RegisterForm
from django.utils import timezone

from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def test(request):
    return render(request, '/Documents/Django/fabric/templates/knitting/test.html',{})


def index(request):

    upcoming_courses=Course.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
    tutors=Tutor.objects.order_by('name').exclude(name='Nikodem') #wylaczamy Nikodema bo on nie jest tutorem a jest w bazie
    context_dict={'categories': upcoming_courses, 'tuts':tutors}
    return render(request, '/Documents/Django/fabric/templates/knitting/indexBase.html' ,context_dict)

def about(request):
    return render(request, '/Documents/Django/fabric/templates/knitting/about.html',{})

def registered(request):
    #odpowiedz na poprawne zarejestrowanie sie
    return HttpResponse('Thanks for registration </br> powrot do strony glownej </br> <a href="/">powrot</a>')
def notregistered(request):
    #odpowiedz gdy wystapil blad w rejestracji:
    return HttpResponse('Registration collapsed please return to registration form <a href="">rejestracja</a>')


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




def course1(request):
    #TODO wyswietlaj plakat na podstawie wybranego kursu
    return render(request, '/Documents/Django/fabric/templates/knitting/course1.html',{})
