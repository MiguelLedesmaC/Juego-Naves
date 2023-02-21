import pygame
import random
import os 

#Directorios
#Directorio principal
carpeta_juego = os.path.dirname(__file__)

#directorio imagenes
#directorio imagenes principal
carpeta_imagenes = os.path.join(carpeta_juego,'imagenes')

#Sub directorio imagenes
carpeta_imagenes_enemigos= os.path.join(carpeta_imagenes,'enemigos')
carpeta_imagenes_personaje = os.path.join(carpeta_imagenes, 'personajes')
carpeta_imagenes_fondos = os.path.join(carpeta_imagenes, 'fondos')
carpeta_imagenes_armas = os.path.join(carpeta_imagenes, 'armas')
carpeta_imagenes_explosiones = os.path.join(carpeta_imagenes, 'meteorito_explosion')

#Directorio de sonido
#directorio sonido principal
carpeta_sonidos = os.path.join(carpeta_juego, 'sonidos')

#Subdirectorio de sonidos
carpeta_sonidos_ambiente = os.path.join(carpeta_sonidos, 'ambiente')
carpeta_sonidos_armas = os.path.join(carpeta_sonidos, 'armas')
carpeta_sonidos_explosiones = os.path.join(carpeta_sonidos, 'explosiones')


#tamaño de la pantalla
ancho = 800
alto = 600
#fondo de pantalla
fondo = pygame.image.load('imagenes/fondos/fondospace.png')
#fps
FPS= 30

#paleta de colores
blanco=(255,255,255)
negro= (0,0,0)
rojo = (255,0,0)
H_FA2F2F = (255,47,47)
verde = (0,255,0)
azul = (0,0,255)
H_50D2FE = (94,210,254)

#fuentes
consolas = pygame.font.match_font('consolas')
times= pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

#sonidos
pygame.mixer.init()
laser = pygame.mixer.Sound(os.path.join(carpeta_sonidos_armas,'laser.wav'))
pygame.mixer.music.load(os.path.join(carpeta_sonidos_ambiente, 'in-orbit-1153.wav'))
explosion_verde = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion1.wav'))
explosion_azul = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion2.wav'))
explosion_rojo = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion3.wav'))
explosion_lila = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion3.wav'))
pygame.mixer.music.play(-1)



explosiones_random=[pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion1.wav')),
					pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion2.wav')),
					pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion3.wav')),
					pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion3.wav'))]



class Jugador (pygame.sprite.Sprite):
	#sprite del jugador
	def __init__(self):

		#heredamos de la superclase
		super().__init__()

		#rectangulo(jugador)

		self.image = pygame.image.load(os.path.join(carpeta_imagenes_personaje,'nave_player.png')).convert()
		#para eliminar un color
		self.image.set_colorkey(negro)

		#obtiene el restangulo(sprite
		self.rect = self.image.get_rect()
		self.radius = 45
		#centra el rectangulo(sprite)
		self.rect.center =(400, 600)
		#velocidad del personaje(inicial)
		self.velocidad_x= 0
		self.velocidad_y= 0
		#disparos
		self.cadencia = 450
		self.ultimo_disparo = pygame.time.get_ticks()
		self.hp =100
		self.vidas = 3

	def update(self):
		#actualiza esto cada vuelta al bucle
		'''self.rect.x -=10
		if self.rect.right < 0:
			self.rect.left = ancho'''

		#velocidad predeterminada cada vuelta del bucle si no pulsas nada
		self.velocidad_x= 0
		self.velocidad_y = 0

		#mantiene las teclas pulsadas
		teclas = pygame.key.get_pressed()

		#mueve el personaje izquierda
		if teclas[pygame.K_a]:
			self.velocidad_x = -15
		#mueve a la derecha
		if teclas[pygame.K_d]:
			self.velocidad_x = +15
		#mueve hacia arriba
		if teclas[pygame.K_w]:
			self.velocidad_y = -15
		#mueve hacia abajo
		if teclas[pygame.K_s]:
			self.velocidad_y = +15
		if teclas[pygame.K_SPACE]:
			tiempo_disparo = pygame.time.get_ticks()
			if tiempo_disparo - self.ultimo_disparo > self.cadencia:
				jugador.disparo()
				self.ultimo_disparo = tiempo_disparo



		#actualiza la posicion del personaje
		self.rect.x += self.velocidad_x
		self.rect.y += self.velocidad_y

		#limita el margen izquierda
		if self.rect.left < 0:
		   self.rect.left = 0

		#limita el margen derecho
		if self.rect.right > ancho:
		   self.rect.right = ancho

		#limita el margen de abajo
		if self.rect.bottom > alto:
		   self.rect.bottom = alto
		#limita el superior
		if self.rect.top < 0:
		   self.rect.top = 0

	def disparo(self):
		bala = Disparos(self.rect.centerx, self.rect.top + 20)
		balas.add(bala)
		laser.play()

class EnemigosAzul(pygame.sprite.Sprite):
	def __init__(self):
		#heredamos el init de pygame
		super().__init__()
		#rectangulo de jugador(sprite)
		self.image =pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigoazul.png'))
		self.image.set_colorkey(blanco)

		self.rect=self.image.get_rect()
		self.radius=45
		self.rect.x=random.randrange(ancho - self.rect.width)
		self.rect.y = random.randrange(alto - self.rect.height)
		self.velocidad_x = random.randrange(1,10)
		self.velocidad_y = random.randrange(1, 10)
		self.hp = 20 

	def update(self):
		#actualiza la velocidad del enemigo
		self.rect.x +=self.velocidad_x
		self.rect.y += self.velocidad_y

		#limita el margen izquierdo
		if self.rect.left < 0:
		   self.velocidad_x +=1

		#limita margen derecho
		if self.rect.right > ancho:
		   self.velocidad_x -=1

		#limita margen inferior
		if self.rect.bottom > alto:
		   self.velocidad_y -=1

		#limita margen superior
		if self.rect.top < 0:
		   self.velocidad_y +=1

class EnemigosRojos(pygame.sprite.Sprite):
	def __init__(self):
		#heredamos el init de pygame
		super().__init__()
		#rectangulo de jugador(sprite)
		self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigorojo.png'))
		self.image.set_colorkey(blanco)

		self.rect=self.image.get_rect()
		self.radius=45
		self.rect.x=random.randrange(ancho - self.rect.width)
		self.rect.y = random.randrange(alto - self.rect.height)
		self.velocidad_x = random.randrange(1,7)
		self.velocidad_y = random.randrange(1, 7)
		self.hp = 15

	def update(self):
		#actualiza la velocidad del enemigo
		self.rect.x +=self.velocidad_x
		self.rect.y += self.velocidad_y

		#limita el margen izquierdo
		if self.rect.left < 0:
			self.velocidad_x +=1

		#limita margen derecho
		if self.rect.right > ancho:
			self.velocidad_x -=1

		#limita margen inferior
		if self.rect.bottom > alto:
			self.velocidad_y -=1

		#limita margen superior
		if self.rect.top < 0:
			self.velocidad_y +=1

class EnemigosLila(pygame.sprite.Sprite):
	def __init__(self):
		#heredamos el init de pygame
		super().__init__()
		#rectangulo de jugador(sprite)
		self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigolila.png'))
		self.image.set_colorkey(blanco)
		self.rect=self.image.get_rect()
		#self.image = pygame.Surface((90,50))
		self.radius = 45
		self.rect.x=random.randrange(ancho - self.rect.width)
		self.rect.y = random.randrange(alto - self.rect.height)
		self.velocidad_x = random.randrange(1,3)
		self.velocidad_y = random.randrange(1, 3)
		self.hp = 10

	def update(self):
		#actualiza la velocidad del enemigo
		self.rect.x +=self.velocidad_x
		self.rect.y += self.velocidad_y

		#limita el margen izquierdo
		if self.rect.left < 0:
			self.velocidad_x +=1

		#limita margen derecho
		if self.rect.right > ancho:
			self.velocidad_x -=1

		#limita margen inferior
		if self.rect.bottom > alto:
			self.velocidad_y -=1

		#limita margen superior
		if self.rect.top < 0:
			self.velocidad_y +=1

class EnemigosVerdes(pygame.sprite.Sprite):
	def __init__(self):
		#heredamos el init de pygame
		super().__init__()
		#rectangulo (jugador)
		self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo3.png')),(80,60))
		self.image.set_colorkey(blanco)

		#obtiene el rectangulo(sprite)
		self.rect = self.image.get_rect()
		self.radius = 45
		self.rect.x= random.randrange(ancho - self.rect.width)
		self.rect.y= random.randrange(alto - self.rect.height)
		self.velocidad_x = random.randrange(3,6)
		self.velocidad_y = random.randrange(3,6)
		self.hp = 15

	def update(self):
		#actualiza velocidad del enemigo
		self.rect.x +=self.velocidad_x
		self.rect.y += self.velocidad_y

		#limita el margen izquierda
		if self.rect.left < 0:
		   self.velocidad_x += 1

		#limita el margen derecho
		if self.rect.right > ancho:
		   self.velocidad_x -=1

		#limita el margen inferior
		if self.rect.bottom > alto:
		   self.velocidad_y -=1
		#limita el superior
		if self.rect.top < 0:
		   self.velocidad_y +=1

class Disparos(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_armas,'disparo.png')).convert(), (10,20))
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x 

	def update(self):
		self.rect.y -= 25
		if self.rect.bottom < 0:
			self.kill()

class Meteoritos(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.img_aleatoria = random.randrange(3)
		if self.img_aleatoria ==0:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes, 'meteorito.png')).convert(),(100,100))
			self.radius=50
		elif self.img_aleatoria ==1:
			 self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes, 'meteorito.png')).convert(),(50,50))
			 self.radius = 25
		elif self.img_aleatoria ==2:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes, 'meteorito.png')).convert(),(25,25))
		self.radius = 12
		self.image.set_colorkey(negro)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ancho - self.rect.width)
		self.rect.y = -self.rect.width
		self.velocidad_y = random.randrange(1, 10)
	def update(self):
		self.rect.y += self.velocidad_y
		if self.rect.top > alto:
			self.rect.x = random.randrange(ancho - self.rect.width)
			self.rect.y = -self.rect.width
			#ancho
			self.velocidad_y = random.randrange(1, 10)

class Explosiones(pygame.sprite.Sprite):
	def __init__(self, centro, dimensiones):
		pygame.sprite.Sprite.__init__(self)
		self.dimensiones = dimensiones
		self.image = animacion_explosion1[self.dimensiones][0]
		self.rect = self.image.get_rect()
		self.rect.center = centro
		self.fotograma = 0 
		self.frecuencia_fotograma = 35
		self.actualizacion = pygame.time.get_ticks()
	def update(self):
		tiempo_disparo = pygame.time.get_ticks()
		if tiempo_disparo - self.actualizacion > self.frecuencia_fotograma:
			self.actualizacion = tiempo_disparo
			self.fotograma +=1
			if self.fotograma == len(animacion_explosion1[self.dimensiones]):
				self.kill()
			else:
				centro = self.rect.center
				self.image = animacion_explosion1[self.dimensiones][self.fotograma]
				self.rect = self.image.get_rect()
				self.rect.center = centro
#Explosiones
animacion_explosion1= {'t1':[],'t2':[],'t3':[],'t4': []}
for x in range (24):
	#creamos variable que 
	archivo_explosiones = f'expl_02_00{x:02d}.png'
	imagenes = pygame.image.load(os.path.join(carpeta_imagenes_explosiones, archivo_explosiones))
	imagenes.set_colorkey(negro)
	imagenes_t1=pygame.transform.scale(imagenes, (32,32))
	animacion_explosion1['t1'].append(imagenes_t1)
	imagenes_t2 = pygame.transform.scale(imagenes, (64,64))
	animacion_explosion1['t2'].append(imagenes_t2)
	imagenes_t3 = pygame.transform.scale(imagenes, (128,128))
	animacion_explosion1['t3'].append(imagenes_t3)
	imagenes_t4 = pygame.transform.scale(imagenes, (256, 256))
	animacion_explosion1['t4'].append(imagenes_t4)



#inicializacion de pygame,creacion de la ventana, titulo y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))

#sistema de puntuaciones
puntuacion = 0

def barra_hp(pantalla, x, y, hp):
	largo = 200
	ancho =25
	calculo_barra = int(jugador.hp /100 * largo)
	borde =pygame.Rect(x, y, largo, ancho)
	rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
	pygame.draw.rect(pantalla, azul, borde, 3)
	pygame.draw.rect(pantalla,H_FA2F2F,rectangulo)
	pantalla.blit(pygame.transform.scale(jugador.image, (25, 25)), (20,15))
	warning= pygame.image.load(os.path.join(carpeta_imagenes_explosiones, 'warning.png'))
	warning.set_colorkey(blanco)
	
	if jugador.hp < 0:
		jugador.hp = 0

	if jugador.hp <45:
		pantalla.blit(pygame.transform.scale(warning, (25,25)),(250,15))

def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y):
	tipo_letra = pygame.font.Font(fuente,dimensiones)
	superficie = tipo_letra.render(texto, True, color)
	rectangulo = superficie.get_rect()
	rectangulo.center = (x, y)
	pantalla.blit(superficie, rectangulo)


pygame.display.set_caption('Alien Invasion')
clock= pygame.time.Clock()

#grupo de sprites, instanciacion del objeto jugador
sprites = pygame.sprite.Group()
enemigos_rojos = pygame.sprite.Group()
enemigos_verdes = pygame.sprite.Group()
enemigos_azules = pygame.sprite.Group()
enemigos_lilas = pygame.sprite.Group()
balas = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()
explosiones = pygame.sprite.Group()
#instaciones de enemigos
enemigo= EnemigosVerdes()
enemigos_verdes.add(enemigo)
enemigo_azul= EnemigosAzul()
enemigos_azules.add(enemigo_azul)
enemigo_lila = EnemigosLila()
enemigos_lilas.add(enemigo_lila)
enemigo_rojo= EnemigosRojos()
enemigos_rojos.add(enemigo_rojo)

#instanciones de jugador principal
jugador = Jugador()
sprites.add(jugador)

#for x in range(3):
#	meteorito = Meteoritos()
#	meteoritos.add(meteorito)

#bucle de juego
ejecutando = True
while ejecutando:
	# es lo que especifica la velocidad del bucle de juego
	clock.tick(FPS)
	#eventos
	for event in pygame.event.get():
	#se cierra y termina el bucle
		if event.type == pygame.QUIT:
			ejecutando = False
		
	#actualizacion de sprites
	sprites.update()
	enemigos_verdes.update()
	enemigos_lilas.update()
	enemigos_rojos.update()
	enemigos_azules.update()
	explosiones.update()
	balas.update()
	meteoritos.update()

	explosion_random= random.randrange(1,4)

	#para unir un sprite con un grupo y se genera una colision
	#colision_nave= pygame.sprite.spritecollide(jugador,enemigos_verdes,False,pygame.sprite.collide_circle)
	#Para unir un grupo de sprites
	colision_disparos_verdes=pygame.sprite.groupcollide(enemigos_verdes, balas, False ,True, pygame.sprite.collide_circle)
	if colision_disparos_verdes:
		puntuacion += 20
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		enemigo.hp -=10
	if enemigo.hp < 0:
		enemigo.kill()



	colision_disparos_azules=pygame.sprite.groupcollide(enemigos_azules, balas, False, True, pygame.sprite.collide_circle)
	if colision_disparos_azules:
		puntuacion += 15
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo_azul.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		enemigo_azul.hp -=10
	if enemigo_azul.hp < 0:  
		enemigo_azul.kill()  

	colision_disparos_rojos=pygame.sprite.groupcollide(enemigos_rojos, balas, False, True, pygame.sprite.collide_circle)
	if colision_disparos_rojos:
		puntuacion += 10
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo_rojo.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		enemigo_rojo.hp -=15
	if enemigo_rojo.hp < 0:
		enemigo_rojo.kill()

	vida3= pantalla.blit(pygame.transform.scale(jugador.image,(25,25)), (510,15))
	vida2= pantalla.blit(pygame.transform.scale(jugador.image,(25,25)), (475,15))
	vida1= pantalla.blit(pygame.transform.scale(jugador.image,(25,25)), (440,15))
	cruz = pygame.image.load(os.path.join(carpeta_imagenes_explosiones, 'tachar.png'))

	if jugador.hp <= 0 and jugador.vidas ==3:
		jugador.kill()
		jugador = Jugador()
		sprites.add(jugador)
		jugador.vidas = 2

	if jugador.vidas ==2:
		if jugador.hp <= 0:
			jugador.kill()
			jugador = Jugador()
			sprites.add(jugador)
			jugador.vidas = 1
	vida1 = pantalla.blit(pygame.transform.scale(cruz, (25,25)),(510,15))

	if jugador.vidas ==1:
		if jugador.hp <= 0:
			jugador.kill()
			jugador = Jugador()
			sprites.add(jugador)
			jugador.vidas = 0
	vida1 = pantalla.blit(pygame.transform.scale(cruz, (25,25)),(510,15))
	vida2 = pantalla.blit(pygame.transform.scale(cruz, (25,25)),(475,15))

	if jugador.vidas ==0:
		if jugador.hp <=0:
			jugador.kill()
			jugador.hp = 0
	vida1 = pantalla.blit(pygame.transform.scale(cruz, (25,25)),(510,15))
	vida2 = pantalla.blit(pygame.transform.scale(cruz, (25,25)),(475,15))
	vida3 = pantalla.blit(pygame.transform.scale(cruz, (25,25)),(475,15))


	colision_disparos_lilas=pygame.sprite.groupcollide(enemigos_lilas, balas, False, True, pygame.sprite.collide_circle)
	if colision_disparos_lilas:
		puntuacion += 50
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo_lila.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		enemigo_lila.hp -=5
	if enemigo_lila.hp < 0:
		enemigo_lila.kill()

	colision_nave_verde = pygame.sprite.spritecollide(jugador,enemigos_verdes,True, pygame.sprite.collide_circle)
	if colision_nave_verde:
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		jugador.hp -=15
		if puntuacion >0:
			puntuacion -=50
			if puntuacion <0:
				puntuacion =0

	colision_nave_rojo = pygame.sprite.spritecollide(jugador, enemigos_rojos, True, pygame.sprite.collide_circle)
	if colision_nave_rojo:
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo_rojo.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		jugador.hp-=25
		if puntuacion >0:
			puntuacion -=15
			if puntuacion <0:
				puntuacion =0

	colision_nave_lila = pygame.sprite.spritecollide(jugador, enemigos_lilas, True, pygame.sprite.collide_circle)
	if colision_nave_lila:
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo_lila.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		jugador.hp -=30
		if puntuacion >0:
			puntuacion -=10
			if puntuacion <0:
				puntuacion =0

	colision_nave_azul = pygame.sprite.spritecollide(jugador, enemigos_azules, True, pygame.sprite.collide_circle)
	if colision_nave_azul:
		explosiones_random[random.randrange(0,3)].play()
		explosion = Explosiones(enemigo_azul.rect.center, f't{explosion_random}')
		explosiones.add(explosion)
		jugador.hp -=50
		if puntuacion >0:
			puntuacion -=5
			if puntuacion <0:
				puntuacion =0


	if jugador.hp <= 0:
		ejecutando = False
		print('GAME OVER')


	

	

	

	#teclas controlar volumen
	keys = pygame.key.get_pressed()
	#baja volumen
	if keys[pygame.K_9] and pygame.mixer.music.get_volume()> 0.0:
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()- 0.1)
	
	
	#sube volumen
	if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+ 0.01)

	elif keys[pygame.K_m]:
		pygame.mixer.music.set_volume(0.0)
		

	#reactivar sonido
	elif keys[pygame.K_COMMA]:
		pygame.mixer.music.set_volume(1.0)

	if not enemigos_lilas and not enemigos_rojos and not enemigos_verdes and not enemigos_azules:
		enemigo= EnemigosVerdes()
		enemigos_verdes.add(enemigo)
		enemigo_azul= EnemigosAzul()
		enemigos_azules.add(enemigo_azul)
		enemigo_lila = EnemigosLila()
		enemigos_lilas.add(enemigo_lila)
		enemigo_rojo= EnemigosRojos()
		enemigos_rojos.add(enemigo_rojo)

	'''if colision_nave:
		enemigo.image= pygame.image.load('imagenes/colision.png')
		enemigo.image.set_colorkey(blanco)
		enemigo.velocidad_y += 10
	elif enemigo.rect.top > alto:
		enemigo.kill()

	elif colision_disparos:
		enemigo.image= pygame.image.load('imagenes/colision.png')
		enemigo.image.set_colorkey(blanco)
		enemigo.velocidad_y += 10
	elif enemigo.rect.top > alto:
		enemigo.kill()'''

	
	#fondo de pantalla, dibujo de sprites y formas geometricas.
	pantalla.blit(fondo, [0,0])
	sprites.draw(pantalla)
	enemigos_lilas.draw(pantalla)
	enemigos_azules.draw(pantalla)
	enemigos_rojos.draw(pantalla)
	enemigos_verdes.draw(pantalla)
	explosiones.draw(pantalla)
	balas.draw(pantalla)
	meteoritos.draw(pantalla)
	#pygame.draw.line(pantalla, H_50D2FE, (400, 0), (400,800),1)
	#pygame.draw.line(pantalla, azul, (0,300), (800, 300),1)

	#dibuja los textos en pantalla
	muestra_texto(pantalla, consolas, str(puntuacion).zfill(6), rojo, 40, 700, 50)
	barra_hp(pantalla, 50, 15,jugador.hp)
	#actualiza el contenido de la pantalla
	pygame.display.flip()
	
pygame.quit()


