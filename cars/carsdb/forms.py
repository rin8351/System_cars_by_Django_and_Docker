from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomParts(forms.ModelMultipleChoiceField):
    def label_from_instance(self, parts):
        return parts.model_p

class AddCars(forms.ModelForm):

    class Meta:
        model = cars
        fields = ['name', 'margin', 'parts']

    name=forms.CharField(max_length=100)
    margin=forms.IntegerField()
    parts=CustomParts(queryset=parts.objects.all(), widget=forms.CheckboxSelectMultiple)

    def create(self, commit=True):
        car = super().save(commit=False)
        car.save()
        for part in self.cleaned_data['parts']:
            car_part.objects.create(car=car, part=part, name=car.name)
        return car

    def save(self, *args, **kwargs):
        self.create()
        super().save(*args, **kwargs)

class AddParts(forms.ModelForm):

    class Meta:
        model = parts
        fields = ['type', 'model_p','price', 'count_p', 'params']

    type=forms.CharField(max_length=100)
    model_p=forms.CharField(max_length=100)
    price=forms.IntegerField()
    count_p=forms.IntegerField()
    params=forms.CharField(max_length=100)


class registeruser(UserCreationForm):
    username= forms.CharField(label = 'Login',widget=forms.TextInput(attrs={'class':'form-input'}))
    email= forms.EmailField(label = 'Email',widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1= forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2= forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
class LoginUserForm(AuthenticationForm):
    username= forms.CharField(label = 'Login',widget=forms.TextInput(attrs={'class':'form-input'}))
    password= forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
