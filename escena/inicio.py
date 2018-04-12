import pilasengine
from actor.fondo import Fondo

class Inicio(pilasengine.escenas.Escena):

	def iniciar(self, pilas):

		texto_codigo = self.pilas.actores.Texto( "Doble Salto !!! V.1.0 (DEMO)", magnitud=30,x=0,y=123)
		texto_codigo.color = pilas.colores.Color(0, 0, 0)
		fondo = Fondo(pilas)
		self.boton = self.pilas.interfaz.Boton("jugar",x=0,y= -123)
		self.boton.conectar(self.cuandoPulsanElBoton)

	def cuandoPulsanElBoton(self):
		self.pilas.escenas.PantallaJuego(pilas=self.pilas)