from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LeadContacto, GaleriaTrabajo # Importante importar ambos
from .forms import ContactoForm

def landing_index(request):
    # Traemos todos los trabajos guardados en el Admin
    trabajos = GaleriaTrabajo.objects.all()
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias! Tu mensaje ha sido enviado.')
            return redirect('index')
    else:
        form = ContactoForm()
    
    # Pasamos 'trabajos' al diccionario de contexto
    return render(request, 'web/index.html', {'form': form, 'trabajos': trabajos})
