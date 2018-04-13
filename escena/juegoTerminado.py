import pilasengine
from actor.fondoDeLadrillos import FondoDeLadrillos

class PantallaJuegoTerminado(pilasengine.escenas.Escena):


    def iniciar(self, pilas, puntaje):

        # se crea el fondo
        self.fondoDeLadrillos = FondoDeLadrillos(pilas)

        #se crea el texto de Juego Terminado
        self.textoJuegoTerminado = self.pilas.actores.Texto("Juego Terminado", magnitud=40)
        self.textoJuegoTerminado.y = 100

        #se crea el texto que muestra el puntaje
        self.textoPuntaje = self.pilas.actores.Texto("puntaje: " + str(puntaje), magnitud=40)

        #se crear los botones con sus respectivas rutas
        self.irAlInicio = self.pilas.interfaz.Boton("ir al inicio",x=123,y=-123)
        self.irAlInicio.conectar(self.cuandoPulsanElBoton)
        self.volverAJugar = self.pilas.interfaz.Boton("volver a jugar",x=-123,y=-123)
        self.volverAJugar.conectar(self.cuandoPulsanElBotonJ)

    def cuandoPulsanElBotonJ(self):
        self.pilas.escenas.PantallaJuego(pilas=self.pilas)

    def cuandoPulsanElBoton(self):
        self.pilas.escenas.Inicio(pilas=self.pilas)

