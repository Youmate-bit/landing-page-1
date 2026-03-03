from django.contrib import admin
from .models import LeadContacto, GaleriaTrabajo

@admin.register(LeadContacto)
class LeadContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'interes', 'creado_el')
    
    list_filter = ('interes', 'creado_el')
    
    search_fields = ('nombre', 'email')
    
    ordering = ('-creado_el',)
    
    readonly_fields = ('creado_el',)

@admin.register(GaleriaTrabajo)
class GaleriaTrabajoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')