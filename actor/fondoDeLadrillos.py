from pilasengine.actores.actor import Actor

class FondoDeLadrillos(Actor):

	def iniciar(self):
		#se le quita la figura de colision al fondo
		self._figura_de_colision = None

		#se le da apariencia y animacion al fondo
		self.imagen = "imagenes/fondo/pared_ladrillo.png"
		self.escala = 0.3
		self.z = 200
		self.imagen.repetir_horizontal = True
		self.imagen.repetir_vertical = True
		self.tarea = self.pilas.tareas.siempre(1 / 90.0, self.moverFondo)

	def moverFondo(self):
		self.y -= 1
