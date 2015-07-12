from django import forms
from knitting.models import UserProfile, Student, Kontakt #import modelu do ktorego robimy formularz
from django.utils import timezone
from django.contrib.auth.models import User

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

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')






class ClientKontakt(forms.ModelForm):
    name=forms.CharField(max_length=25, help_text="Imie")
    email=forms.EmailField(help_text="email")
    message=forms.TextInput()
    date=forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)

    class Meta:
            model = Kontakt     #zapis metadanych do ktorego modelu odnosi sie formularz
            fields = ( 'name','email', 'message')    #i jakie pola ma zawierac
