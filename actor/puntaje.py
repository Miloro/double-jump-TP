from pilasengine.actores.actor import Actor
from pilasengine.colores import *

class Puntaje(Actor):

    def iniciar(self, x=0, y=0):
        #se le coloco un marco
        self.imagen = "imagenes/actor/puntos.png"

        #se escala la imagen
        self.escala = 2

        #se inicia el puntaje en 1
        self.puntos = 1

        #se crea el texto del puntaje y se lo acoomoda
        self.texto = self.pilas.actores.Texto("Puntaje: " + str(self.puntos),magnitud= 20 ,fuente="imagenes/fuentes/ice_pixel-7.ttf")
        self.texto.x = x + 28
        self.texto.y = y -2
        self.texto.ancho = 200
        self.texto.escala = 0.6
        self.texto.color = negro

        #se crea la tarea que aumpenta un punto por segundo
        self.tarea_en_curso = self.pilas.tareas.siempre(1, self.aumentarPuntos)

    # aumenta un punto al puntaje
    def aumentarPuntos(self):
        self.puntos += 1
        self.actualizarTexto()

    # actualiza el texto
    def actualizarTexto(self):
        self.texto.texto = ("puntaje: " + str(self.puntos))


