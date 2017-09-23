from pilasengine.actores.actor import Actor


class Plataforma(Actor):

    def iniciar(self):
      self.imagen = "imagenes/actor/plataforma.png"
      self.escala = 1
      self.figura = self.pilas.fisica.Rectangulo(-180,self.y,270,15,False,self.x,self.y,450,30,True,False,True)



    def actualizar(self):
        self.figura.x = self.x
        self.figura.y = self.y
        self.y = -100



