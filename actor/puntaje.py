from pilasengine.actores.actor import Actor
from pilasengine.colores import *

class Puntaje(Actor):

    def iniciar(self, x=0, y=0):
        self.imagen = "imagenes/actor/puntos.png"
        self.escala = 2
        self.puntos = 1
        self.tarea_en_curso = self.pilas.tareas.siempre(1, self.aumentarPuntos)
        self.texto = self.pilas.actores.Texto("Puntaje: " + str(self.puntos),magnitud= 20 ,fuente="imagenes/fuentes/ice_pixel-7.ttf")
        self.texto.x = x + 28
        self.texto.y = y -2
        self.texto.ancho = 200
        self.texto.escala = 0.6
        self.texto.color = negro


    def comenzar(self):
        if self.tarea_en_curso == None: 
            self.tarea_en_curso = self.pilas.tareas.siempre(1, self.aumentarPuntos)

    def aumentarPuntos(self):
        self.puntos += 1
        self.actualizarTexto()

    def actualizarTexto(self):
        self.texto.texto = ("puntaje: " + str(self.puntos))


