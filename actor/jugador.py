from pilasengine.actores.actor import Actor


class Jugador(Actor):
    def iniciar(self):
        self.velocidad_x = 5
        self.imagen = "imagenes/actor/player.png"
        self.escala = 1
        self._figura_de_colision = self.pilas.fisica.Rectangulo(self.x, self.y, ancho = 20 , alto = 44 , sensor=False, dinamica= True, restitucion= 0.000001, densidad= 1)

        self._figura_de_colision.sin_rotacion = True
        self._figura_de_colision.escala_de_gravedad = 3.5

        self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)

    def actualizar(self):

        velocidad = 10
        salto = 20
        self.x = self._figura_de_colision.x
        self.y = self._figura_de_colision.y

        if self.pilas.control.derecha:
            self._figura_de_colision.velocidad_x = velocidad
            self.espejado = True
        elif self.pilas.control.izquierda:
            self._figura_de_colision.velocidad_x = -velocidad
            self.espejado = False
        else:
            self._figura_de_colision.velocidad_x = 0

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self._figura_de_colision.velocidad_y) <= 0:
                self._figura_de_colision.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 27

        if self.esta_pisando_el_suelo():
            self.imagen = "imagenes/actor/player.png"
        else:
            self.imagen = "imagenes/actor/player.png"

        if self.x > 330:
            self.x = -330
            self._figura_de_colision.x = -330

        if self.x < -330:
            self.x = +330
            self._figura_de_colision.x = 330

    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0
