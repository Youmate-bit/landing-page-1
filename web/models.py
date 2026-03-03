from django.db import models

class LeadContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    interes = models.CharField(max_length=50, choices=[
        ('maquillaje', 'Maquillaje Social'),
        ('cursos', 'Cursos de Automaquillaje'),
        ('productos', 'Consulta de Productos')
    ])
    mensaje = models.TextField()
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class GaleriaTrabajo(models.Model):
    titulo = models.CharField(max_length=100)
    # Cambia upload_url por upload_to aquí:
    foto_antes = models.ImageField(upload_to='galeria/') 
    foto_despues = models.ImageField(upload_to='galeria/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
