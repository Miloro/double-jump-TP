import pilasengine
from escena.inicio import Inicio
from escena.juegoTerminado import PantallaJuegoTerminado
from escena.pantallaJuego import PantallaJuego


pilas = pilasengine.iniciar(titulo='salto-doble 0.2', habilitar_mensajes_log=False)

# se vinculan todas las escenas y se inicia en la de inicio
pilas.escenas.vincular(PantallaJuegoTerminado)
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(Inicio)
pilas.escenas.Inicio(pilas=pilas)
pilas.ejecutar()