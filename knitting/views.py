from django.shortcuts import render
from django.http import HttpResponse
from knitting.models import Student, Course, Tutor
from knitting.forms import RegisterForm, ClientKontakt
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
    if not request.user.is_authenticated():
        return render(request, '/Documents/Django/fabric/templates/knitting/indexBase.html' ,context_dict)
    else:
        return HttpResponse("You are not logged in.")


def about(request):
    return render(request, '/Documents/Django/fabric/templates/knitting/about.html',{})

def registered(request):
    #odpowiedz na poprawne zarejestrowanie sie
    return HttpResponse('Thanks for registration </br> powrot do strony glownej </br> <a href="/">powrot</a>')
def notregistered(request):
    #odpowiedz gdy wystapil blad w rejestracji:
    return HttpResponse('Registration collapsed please return to registration form <a href="">rejestracja</a>')




def course1(request):
    #TODO wyswietlaj plakat na podstawie wybranego kursu
    return render(request, '/Documents/Django/fabric/templates/knitting/course1.html',{})



'''
View for new usrers' registration
'''
from knitting.forms import UserForm, UserProfileForm


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            '/Documents/Django/fabric/templates/knitting/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


'''
login
'''
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Fabric <action> account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, '/Documents/Django/fabric/templates/knitting/login.html', {})





"""
def resume(request):
    return render(request, '/Documents/Django/fabric/templates/resume.html',{})

"""
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

def notcontact(request):
    #odpowiedz gdy wystapil blad w rejestracji:
    return HttpResponse('Contact collapsed please return to main page <a href="/resume/">powrot</a>')



def resume(request):
    #glowny watek rejestracji
    if request.method == 'POST':
        form=ClientKontakt(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, '/Documents/Django/fabric/templates/resume.html',{'form':form})
        else:
            return notcontact(request)
    else:
        form=ClientKontakt()
    return render(request, '/Documents/Django/fabric/templates/resume.html',{'form':form})

def resumefp(request):
    #glowny watek rejestracji
    if request.method == 'POST':
        form=ClientKontakt(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, '/Documents/Django/fabric/templates/resumefp.html',{'form':form})
        else:
            return notcontact(request)
    else:
        form=ClientKontakt()
    return render(request, '/Documents/Django/fabric/templates/resumefp.html',{'form':form})

