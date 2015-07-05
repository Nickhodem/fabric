# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
from swop.forms import ProfileImageForm
from swop.models import ProfileImage

class ProfileImageView(FormView):
    template_name = '/Documents/Django/fabric/templates/swop/profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image=ProfileImage(image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id=profile_image.id
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return HttpResponse('Thanks for uploading </br> powrot do strony glownej </br> <a href="http://127.0.0.1:8000/">powrot</a>')

        return reverse('profile_image', kwargs={'pk':self.id})

class ProfileDetailView(DetailView):
    model=ProfileImage
    template_name = '/Documents/Django/fabric/templates/swop/profile_image.html'
    context_object_name = 'image'
class ProfileImageIndexView(ListView):
    model=ProfileImage
    template_name = '/Documents/Django/fabric/templates/swop/profil_image_view.html'
    context_object_name = 'images'
    queryset = ProfileImage.objects.all()


def swopengine(request):

    category_list=ProfileImage.objects.all()
    context_dict={'categories': category_list}

    return render(request,'/Documents/Django/fabric/templates/swop/swopengine.html', context_dict)
'''
def swopengine(request):

    return HttpResponse('Lets <a href="/swop/upload/">upload</a> your files')
'''

def uploaded():
    #odpowiedz na poprawne zarejestrowanie sie
    return HttpResponse('Thanks for uploading </br> powrot do strony glownej </br> <a href="http://127.0.0.1:8000/">powrot</a>')




'''

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #file is saved
            form.save()
            return uploaded(request)
    else:
        form=DocumentForm()
    return render(request,'/Documents/Django/fabric/templates/swop/list.html', {'form': form})


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('swop.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        '/Documents/Django/fabric/templates/swop/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
'''