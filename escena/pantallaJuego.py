import pilasengine
from actor.jugador import Jugador
from actor.fondoDeLadrillos import FondoDeLadrillos
from actor.puntaje import Puntaje
from actor.plataformaConMovimiento import PlataformaConMovimiento

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas):

        #se eliminan las paredes de la escena
        pilas.fisica.eliminar_paredes()
        pilas.fisica.eliminar_suelo()
        pilas.fisica.eliminar_techo()

        #se crea una tarea que crea plataformas
        self.tarea = self.pilas.tareas.siempre(2, self.crearPlataformas)

        #se crea una tarea que verifica si el jugador perdio
        self.tarea2 = self.pilas.tareas.siempre(0.1, self.perder)

        #se crea el fondo
        fondo = FondoDeLadrillos(pilas)

        #se crea el puntaje
        self.puntaje = Puntaje(pilas,x = -240, y = 210)

        #se crea el jugador
        self.jugador = Jugador(pilas)

        #se crean las primeras plataformas que aparecen en la escena
        self.plataforma1 = PlataformaConMovimiento(pilas)
        self.plataforma1.y = -100
        self.plataforma1.x = 0
        self.plataforma2 = PlataformaConMovimiento(pilas)
        self.plataforma2.y = 0
        self.plataforma3 = PlataformaConMovimiento(pilas)
        self.plataforma3.y = 100
        self.plataforma4 = PlataformaConMovimiento(pilas)
        self.plataforma4.y = 200
        self.plataforma5 = PlataformaConMovimiento(pilas)
        self.plataforma5.y = 300

    # crea una plataforma
    def crearPlataformas(self):
    	plataformaCM = PlataformaConMovimiento(self.pilas, self.puntaje.puntos)
        plataformaCM.y = 300

    # si el y del jugador es menor o igual a -250 el jugador pierde
    def perder(self):
        if(self.jugador.y <= -250):
            self.pilas.escenas.PantallaJuegoTerminado(pilas=self.pilas, puntaje=self.puntaje.puntos)
