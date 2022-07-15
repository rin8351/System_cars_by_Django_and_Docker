from django import forms
from .models import *

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