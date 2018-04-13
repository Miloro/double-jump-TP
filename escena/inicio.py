import pilasengine
from actor.fondoDeLadrillos import FondoDeLadrillos

class Inicio(pilasengine.escenas.Escena):

	def iniciar(self, pilas):

        #se crea el texto del titulo
		texto_codigo = self.pilas.actores.Texto( "Doble Salto!", magnitud=25,x=0,y=123,fuente = "imagenes/fuentes/Big_Pixel_Shadow_demo.otf")
		texto_codigo.color = pilas.colores.Color(0, 0, 0)

        #se crea el marco del titulo
		marco = pilas.imagenes.cargar("imagenes/actor/marco_titulo.png")
		marcoTitulo = pilas.actores.Actor()
		marcoTitulo.imagen = marco
		marcoTitulo.y = 123
		marcoTitulo.escala=3

        #se crea el fondo
		self.fondoDeLadrillos = FondoDeLadrillos(pilas)

        #se crea el boton
		self.boton = self.pilas.interfaz.Boton("jugar",x=0,y= -123)
		self.boton.conectar(self.cuandoPulsanElBoton)

	def cuandoPulsanElBoton(self):
		self.pilas.escenas.PantallaJuego(pilas=self.pilas)