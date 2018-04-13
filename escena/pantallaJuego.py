import pilasengine
from actor.jugador import Jugador
from actor.fondo import Fondo
from actor.puntaje import Puntaje
from actor.plataformaConMovimiento import PlataformaCM

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        pilas.fisica.eliminar_paredes()
        pilas.fisica.eliminar_suelo()
        pilas.escena.fisica.eliminar_techo()
        self.tarea = self.pilas.tareas.siempre(2, self.crearPlataformas)
        self.tarea2 = self.pilas.tareas.siempre(0.1, self.perder)
        fondo = Fondo(pilas)
        self.puntaje = Puntaje(pilas,x = -240, y = 210)
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


    def crearPlataformas(self):
    	plataformaCM = PlataformaCM(self.pilas,  self.puntaje.puntos )
        plataformaCM.y = 300

    def perder(self):
        if(self.jugador.y <= -250):
            self.pilas.escenas.PantallaJuegoTerminado(pilas=self.pilas, p=self.puntaje.puntos)
