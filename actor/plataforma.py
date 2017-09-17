# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

#from logica.comportamientos import ComportamientoSaltar

class Plataforma(Actor):

    def iniciar(self):
      self.x = self.pilas.azar(-250, 250)
      self.imagen = "imagenes/actor/plataforma.png"
      self.escala = 1
      self.figura = self.pilas.fisica.Rectangulo(-180,self.y,270,15,False,self.x,self.y,450,30,True,False,True)
       # self.figura = self.pilas.fisica.Circulo(self.x, self.y, 17,friccion=0, restitucion=0)#puede que sea mierda
        #self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)


    def actualizar(self):
        self.figura.x = self.x
        self.figura.y = self.y
        self.y = [-100, 100]