from pilasengine.actores.actor import Actor


class Jugador(Actor):
    def iniciar(self):

        # se le da una imagen al personaje
        self.imagen = "imagenes/actor/player.png"

        # se le da una figura de colision al personaje
        self._figura_de_colision = self.pilas.fisica.Rectangulo(self.x, self.y, ancho = 20 , alto = 44 , sensor=False, dinamica= True, restitucion= 0.000001, densidad= 1)
        self._figura_de_colision.sin_rotacion = True
        self._figura_de_colision.escala_de_gravedad = 3.5

        # s le da un sensor en los pies al personaje
        self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 15, 5, sensor=True, dinamica=False)

    def actualizar(self):
        # se le da una velocidad y una fuerza de salto al personaje
        velocidad = 10
        salto = 20

        # cambia la imagen del personaje si esta saltando
        if self.esta_pisando_el_suelo():
            self.imagen = "imagenes/actor/player.png"
        else:
            self.imagen = "imagenes/actor/player_saltando.png"

        # el personaje siempre queda adentro de la figura de colision
        self.x = self._figura_de_colision.x
        self.y = self._figura_de_colision.y

        # el sensor de pies sigue al personaje
        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 27

        #caso de apretar el boton de la derecha
        if self.pilas.control.derecha:
            self._figura_de_colision.velocidad_x = velocidad
            self.espejado = True
        #caso de apretar el boton de la izquierda
        elif self.pilas.control.izquierda:
            self._figura_de_colision.velocidad_x = -velocidad
            self.espejado = False
        #caso de no apretar ningun boton
        else:
            self._figura_de_colision.velocidad_x = 0

        #el personaje no puede saltar si no esta pisando el suelo
        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self._figura_de_colision.velocidad_y) <= 0:
                self._figura_de_colision.impulsar(0, salto)

        # si el personaje llega a un extremo de la pantalla automaticamente pasa al otro lado
        if self.x > 330:
            self.x = -330
            self._figura_de_colision.x = -330

        if self.x < -330:
            self.x = +330
            self._figura_de_colision.x = 330

    # verifica si esta pisando el suelo
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0
