class ComportamientoSaltar(pilasengine.comportamientos.Comportamiento):

    def iniciar(self, receptor):
        self.receptor = receptor
        #self.receptor.imagen.cargar_animacion('saltar')
        self.velocidad = 12
        self.coordenada_y_inicial = self.receptor.y

    def actualizar(self):
        self.receptor.y += self.velocidad
        self.velocidad -= 0.5

        if self.receptor.y < self.coordenada_y_inicial:
         #   self.receptor.hacer_inmediatamente('ComportamientoNormal')
            self.receptor.y = self.coordenada_y_inicial