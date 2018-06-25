from django import forms
from .models import Cliente

class Cliente(forms.ModelForm):
    class Meta:
                model=Cliente
                fields = ['user','email','senha','mensagem','contato']
