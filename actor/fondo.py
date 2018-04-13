from pilasengine.actores.actor import Actor

class Fondo(Actor):

	def iniciar(self):
		self._figura_de_colision = None
		self.imagen = "invisible.png"
		self.fondo = self.pilas.actores.Actor()
		self.fondo.imagen = "imagenes/fondo/pared_ladrillo.png"
		self.fondo.escala = 0.3
		self.fondo.z = 200
		self.fondo.imagen.repetir_horizontal = True
		self.fondo.imagen.repetir_vertical = True
		self.tarea = self.pilas.tareas.siempre(1/90.0, self.mover_fondo)

	def mover_fondo(self):
		self.fondo.y -= 1
