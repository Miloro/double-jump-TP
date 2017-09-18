import pilasengine
from escena.pantallaJuego import PantallaJuego

pilas = pilasengine.iniciar(titulo='double-jump 0.1 - alpha', habilitar_mensajes_log=False)

pilas.escenas.vincular(PantallaJuego)
pilas.escenas.PantallaJuego(pilas=pilas)
pilas.ejecutar()