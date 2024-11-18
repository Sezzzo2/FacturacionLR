# Empleado/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Empleado
        fields = ['rol']
    
    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username']
        )
        user.set_password(self.cleaned_data['password'])  
        if commit:
            user.save()
            empleado = super().save(commit=False)
            empleado.user = user
            empleado.save()
        return empleado
