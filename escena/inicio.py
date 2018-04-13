import pilasengine
from actor.fondo import Fondo

class Inicio(pilasengine.escenas.Escena):

	def iniciar(self, pilas):

		texto_codigo = self.pilas.actores.Texto( "Doble Salto!", magnitud=25,x=0,y=123,fuente = "imagenes/fuentes/Big_Pixel_Shadow_demo.otf")
		imagen = pilas.imagenes.cargar("imagenes/actor/marco_titulo.png")
		marcoTitulo = pilas.actores.Actor()
		marcoTitulo.imagen = imagen
		marcoTitulo.y = 123
		marcoTitulo.escala=3
		texto_codigo.color = pilas.colores.Color(0, 0, 0)
		fondo = Fondo(pilas)
		self.boton = self.pilas.interfaz.Boton("jugar",x=0,y= -123)
		self.boton.conectar(self.cuandoPulsanElBoton)

	def cuandoPulsanElBoton(self):
		self.pilas.escenas.PantallaJuego(pilas=self.pilas)