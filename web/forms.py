from django import forms
from .models import LeadContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = LeadContacto
        fields = ['nombre', 'email', 'interes', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-lg border-2 border-pink-100 focus:border-pink-500 outline-none transition-all',
                'placeholder': 'Tu nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 rounded-lg border-2 border-pink-100 focus:border-pink-500 outline-none transition-all',
                'placeholder': 'tu@email.com'
            }),
            'interes': forms.Select(attrs={
                'class': 'w-full p-3 rounded-lg border-2 border-pink-100 focus:border-pink-500 outline-none transition-all'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-lg border-2 border-pink-100 focus:border-pink-500 outline-none transition-all',
                'rows': 4,
                'placeholder': '¿En qué podemos ayudarte?'
            }),
        }
