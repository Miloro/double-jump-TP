import pilasengine
from actor.player import Player

class PantallaJuego(pilasengine.escenas.Escena):


    def iniciar(self, pilas):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.jugador = Player(pilas)

