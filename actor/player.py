# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Player(Actor):

    def iniciar(self):
        self.imagen = "imagenes/actor/player.png"
        self.escala = 1
