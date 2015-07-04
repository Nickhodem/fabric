from django import forms
from knitting.models import Student #import modelu do ktorego robimy formularz
from django.utils import timezone

class RegisterForm(forms.ModelForm):
    '''
    Uzupelnienie formularza o wymagane dane w przypadku gdy sa dane ktorych uczestnik nie podaje
    mozna zrobic ukryte pole np:
    created_date=forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)
    '''
    name=forms.CharField(max_length=25, help_text="Imie")
    surname=forms.CharField(max_length=30, help_text="Nazwisko")
    hashname=forms.CharField(max_length=30, help_text="jak mamy sie do Ciebie zwracac?[ksywa]")
    email=forms.EmailField(help_text="email")
    registered_day=forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)

    class Meta:
        model = Student     #zapis metadanych do ktorego modelu odnosi sie formularz
        fields = ( 'name','surname', 'hashname','email')    #i jakie pola ma zawierac