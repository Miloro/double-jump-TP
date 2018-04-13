from pilasengine.actores.actor import Actor


class PlataformaConMovimiento(Actor):

    def iniciar(self, d = 1):

        #se le da una imagen
        self.imagen = "imagenes/actor/plataforma_larga.png"
        self.x = self.pilas.azar(-250, 250)

        #se crea la figura de colision
        self._figura_de_colision = self.pilas.fisica.Rectangulo(self.x,300,270,15,False,self.x,self.y,450,30,True,False,True)

        # se crea una variable que define la dificultad
        self.dificultad = d

        #la escala de la plataforma se define segun la dificultad
        self.escala = 1 - (self.dificultad * 0.01)
        self._figura_de_colision.escala = 1 - (self.dificultad * 0.01)

 

    #hace que la plataforma baje
    def actualizar(self):
        self.y =  self.y - 1
        self._figura_de_colision.y = self.y
        if self.y < -400:
          self.eliminar()