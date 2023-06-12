from django import forms
from django.forms import ModelForm
from .models import *


class FormacaoForm(ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

class ParticipacaoForm(ModelForm):
    class Meta:
        model = Participacao
        fields = '__all__'

class InteresseForm(ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'
