# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Player(Actor):

    def iniciar(self):
    	self.VELOCIDAD = 5
        self.y = -155
        self.escala = 0.75
        self.radio_de_colision = 30
        self.imagen = "imagenes/actor/player.png"
        self.escala = 1


    def actualizar(self):
        if self.pilas.control.izquierda:
            self.x -= self.VELOCIDAD
            self.espejado = False

        if self.pilas.control.derecha:
            self.x += self.VELOCIDAD
            self.espejado = True

        if self.x > 280:
            self.x = 280

        if self.x < -280:
            self.x = -280


