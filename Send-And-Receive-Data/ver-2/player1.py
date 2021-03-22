"""from thinker *
from thinker import filedialog
import pygame 

root = tk()"""

from pygame import mixer

mixer.init()
cancion=str(input("seleccione la cancion: "))
mixer.music.load(cancion)
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print('Pulsa p para detenter la cancion')
    print('Pulsa r para reanudar la cancion')
    print('pulsa e para elegir otra cancion')
    print('Pulsa s para salir')

    opcion = input(">>> ")

    if opcion=="p":
        mixer.music.pause()
    elif opcion=="r":
        mixer.music.unpause()
    elif opcion=="s":
        mixer.music.stop()
        break
    elif opcion=="e":
        mixer.music.stop
        cancion=str(input('Seleccione la cancion: '))
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()