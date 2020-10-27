from django.db import models

class Pregunta_Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_categoria

class Pregunta(models.Model):
    titulo_pregunta = models.CharField(max_length=500)
    contenido_pregunta = models.TextField()
    pregunta_categoria = models.ForeignKey(Pregunta_Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_pregunta
