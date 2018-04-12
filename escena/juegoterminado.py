import pilasengine

class PantallaJuegoTerminado(pilasengine.escenas.Escena):


    def iniciar(self, pilas, p):
        texto_codigo = self.pilas.actores.Texto("Juego Terminado", magnitud=40)
        texto_codigo2 = self.pilas.actores.Texto("puntaje: " + str(p) , magnitud=40)
        texto_codigo2.y = 100

        self.irAlInicio = self.pilas.interfaz.Boton("ir al inicio",x=123,y=-123)
        self.irAlInicio.conectar(self.cuandoPulsanElBoton)
        self.volverAJugar = self.pilas.interfaz.Boton("jugar",x=-123,y=-123)
        self.volverAJugar.conectar(self.cuandoPulsanElBoton)

    def cuandoPulsanElBoton(self):
        self.pilas.escenas.PantallaJuego(pilas=self.pilas)

    def cuandoPulsanElBoton(self):
        self.pilas.escenas.Inicio(pilas=self.pilas)

