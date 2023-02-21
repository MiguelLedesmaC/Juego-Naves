from pygame.locals import*
import pygame,sys
#import os

#iniciacion de pygame
pygame.init()

#pantalla ventana
w,h=1000,600
pantalla= pygame.display.set_mode((w,h))
pygame.display.set_caption('Exterminator')
icono = pygame.image.load('imagenes/jugador.png')
pygame.display.set_icon(icono)

#fondo del juego
fondo=pygame.image.load('imagenes/ciudad.jpg').convert()
x=0
y=0
pantalla.blit(fondo, (x, y))
#musica de fondo
pygame.mixer.music.load('musica/Heroic Intrusion.ogg')
pygame.mixer.music.play(-1)



#personaje
quieto = pygame.image.load('imagenes/quieto2.png')

caminaDerecha = [pygame.image.load('imagenes/run1.png'),
				 pygame.image.load('imagenes/run2.png'),
				 pygame.image.load('imagenes/run3.png'),
				 pygame.image.load('imagenes/run4.png'),
				 pygame.image.load('imagenes/run5.png'),
				 pygame.image.load('imagenes/run6.png')]
 
caminaIzquierda = [pygame.image.load('imagenes/run izquierda1.png'),
				   pygame.image.load('imagenes/run izquierda2.png'),
				   pygame.image.load('imagenes/run izquierda3.png'),
				   pygame.image.load('imagenes/run izquierda4.png'),
				   pygame.image.load('imagenes/run izquierda5.png'),
				   pygame.image.load('imagenes/run izquierda6.png'),]

salta=[pygame.image.load('imagenes/salto1.png'),
	   pygame.image.load('imagenes/salto2.png')]

#Sonido
sonido_arriba = pygame.image.load('imagenes/volume_up.png')
sonido_abajo = pygame.image.load('imagenes/bajar_volumen.png')
sonido_mute = pygame.image.load('imagenes/mute.png')
sonido_max = pygame.image.load('imagenes/vol_max.png')

x=0
px=50
py=200
ancho=40
velocidad=10

#control fps
reloj=pygame.time.Clock()

#variable salto
salto= False

#contador de salto
cuentaSalto=10

#variables direccion
izquierda= False
derecha = False

#pasos
cuentaPasos = 0

#movimiento
def recarga_pantalla():
	#variables globales
	global cuentaPasos
	global x

	#fondo en movimiento
	x_relativa = x % fondo.get_rect().width
	pantalla.blit(fondo, (x_relativa - fondo.get_rect().width,0))
	if x_relativa < w:
		pantalla.blit(fondo,(x_relativa,0))

	x -= 5

	#contador de pasos
	if cuentaPasos +1 >=6:
		cuentaPasos = 0

	#movimiento a la izquierda
	if izquierda:
		pantalla.blit(caminaIzquierda[cuentaPasos // 1],(int(px), int(py)))
		cuentaPasos += 1

	#movimiento a la derecha
	elif derecha:
		pantalla.blit(caminaDerecha[cuentaPasos // 1],(int(px),int(py)))
		cuentaPasos += 1

	elif salto + 1 >= 2:
		pantalla.blit(salta[cuentaPasos // 1],(int(px), int(py)))
		cuentaPasos+=1

	else:
		pantalla.blit(quieto,(int(px),int(py)))

	#actualizacion de pantalla
	pygame.display.update()

ejecuta= True

#bucle de acciones y controles
while ejecuta:	
	#fps
	reloj.tick(18)

	#bucle del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecuta = False

	#opcion tecla pulsada
	keys= pygame.key.get_pressed()

	#tecla A- movimiento izquierda
	if keys[pygame.K_a] and px > velocidad:
		px -= velocidad
		izquierda = True
		derecha = False

	#tecla D -movimiento derecha
	elif keys[pygame.K_d] and px < 900 - velocidad- ancho:
		px += velocidad
		izquierda= False
		derecha= True

	#personaje quieto
	else:
		izquierda= False
		derecha= False
		cuentaPasos=0

	#tecla w- movimiento arriba
	if keys[pygame.K_w] and py > 100:
		py -= velocidad

	#tecla S- movimiento abajo
	if keys[pygame.K_s] and py < 300:
		py += velocidad

	#tecla space - salto
	if not (salto):
		if keys	[pygame.K_SPACE]:
			salto= True
			izquierda= False
			derecha= False
			cuentaPasos= 0

	else:
		if cuentaSalto >= -10:
			py -= (cuentaSalto * abs(cuentaSalto))*0.5
			cuentaSalto -= 1

		else:
			cuentaSalto= 10
			salto= False


	#control de audio

	#baja volumen
	if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
		pantalla.blit(sonido_abajo, (850, 25))
	elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
		pantalla.blit(sonido_mute, (850, 25))
	
	#sube volumen
	if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
		pantalla.blit(sonido_arriba, (850,25))
	elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
		pantalla.blit(sonido_max, (850, 25))

	#desactivar sonido
	elif keys[pygame.K_m]:
		pygame.mixer.music.set_volume(0.0)
		pantalla.blit(sonido_mute, (850, 25))

	#reactivar sonido
	elif keys[pygame.K_COMMA]:
		pygame.mixer.music.set_volume(1.0)
		pantalla.blit(sonido_max, (850, 25))




	pantalla
	#actualizacion de ventana
	pygame.display.update()
	#llamada a la funcion de actualizacion de ventana
	recarga_pantalla()


#salida del juego
pygame.quit()








	
	