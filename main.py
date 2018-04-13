import pilasengine
from escena.inicio import Inicio
from escena.juegoterminado import PantallaJuegoTerminado
from escena.pantallaJuego import PantallaJuego

pilas = pilasengine.iniciar(titulo='salto-doble 0.2', habilitar_mensajes_log=False)


pilas.escenas.vincular(PantallaJuegoTerminado)
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(Inicio)
pilas.escenas.Inicio(pilas=pilas)
pilas.ejecutar()