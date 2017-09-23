import pilasengine
from actor.jugador import Jugador
from actor.plataforma import Plataforma
from actor.fondo import Fondo
from actor.puntaje import Puntaje
from actor.plataformaConMovimiento import PlataformaCM
from logica.cde import CDE

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        self.cde = CDE(self.pilas)
        self.tarea = self.pilas.tareas.siempre(1.2, self.crearPlataformas)
        self.tarea2 = self.pilas.tareas.siempre(0.1, self.perder)
        fondo = Fondo(pilas)
        self.jugador = Jugador(pilas)
        self.plataforma1 = PlataformaCM(pilas)
        self.plataforma1.y = -100
        self.plataforma1.x = 0
        self.plataforma1.figura.x = 0
        self.plataforma2 = PlataformaCM(pilas)
        self.plataforma2.y = 0
        self.plataforma3 = PlataformaCM(pilas)
        self.plataforma3.y = 100
        self.plataforma4 = PlataformaCM(pilas)
        self.plataforma4.y = 200
        self.plataforma5 = PlataformaCM(pilas)
        self.plataforma5.y = 300
        self.puntaje = Puntaje(pilas,x = -230, y = 220)

    def crearPlataformas(self):
    	plataformaCM = PlataformaCM(self.pilas,  self.puntaje.puntos )
        plataformaCM.y = 300

    def perder(self):
        if(self.jugador.y <= -220):
            print("perdiste guchin")
            self.cde.irALaPantallaPerder(self.puntaje.puntos)
