import pilasengine
from actor.jugador import Jugador
from actor.plataforma import Plataforma
from actor.plataformaConMovimiento import PlataformaCM

class PantallaJuego(pilasengine.escenas.Escena):


    def iniciar(self, pilas):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.jugador = Jugador(pilas)
        self.plataforma = Plataforma(pilas)
        self.plataformaCMn = PlataformaCM(pilas)
        self.jugador.y = 400
        self.plataforma.y = -180
        self.plataformaCMn.y = 300 
        self.plataforma.y = [-100, 100, -100, 100,-100, 100,-100, 100,-100, 100,-100]

    def crearPlataformas():
    	plataformaCM = PlataformaCM()
    	plataformaCM = 400

   # def actualizar():
    #	self.tarea = self.pilas.tareas.siempre(0.1, self.crearPlataformas)

   # def actualizar():
        #self.tarea = self.pilas.tareas.siempre(0.1, crearPlataformas)