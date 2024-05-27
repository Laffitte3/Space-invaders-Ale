import pygame
import math
import random


pygame.init()


ancho=800
largo=600

#colores para las letras

black=(0,0,0)
white=(255,255,255)

#Fotogramas por segundo
FPS= 30
reloj=pygame.time.Clock()

#Cantidad de enemigos que yo quiero tener en el juego
nuemro_de_enemigos= 8

#Puntos del juego
puntos= 0


#Alien atributos
#Si vamos a crear varios alienigenas necesito crear listas por lo cual este ya no me sirve
alien_x_change= 5
alien_y_change= 40
alien_x_random= random.randint(0,ancho)
alien_y_random=random.randint(50,150)

#Si vamos a crear varios alienigenas utilizamos listas
"""alien_x_change= []
alien_y_change= []
alien_x_random= []
alien_y_random= []
"""

#Proyectil atributos

bullet_x_change= 0
bullet_y_change= 15
bullet_state="ready"


#Icono del proyecto

icono= pygame.image.load("ufo.png")
pygame.display.set_icon(icono)

#Crear la pantalla

pantalla= pygame.display.set_mode((ancho,largo))


#Añadir fondo de pantalla
fondo= pygame.image.load("fedex.jfif")
fondo= pygame.transform.scale(fondo,(ancho,largo))


#Añadir Sprites a los personajes

player= pygame.image.load("player.png")
bullet= pygame.image.load("tomato.png")
bullet=pygame.transform.scale(bullet,(60,60))
alien=pygame.image.load("alien33.png")
#alien=[]

#Crear rectangulo de las imagenes

player_rect= player.get_rect()
bullet_rect= bullet.get_rect()
#Al utilizar listas, este alien rect queda invaidado
#alien_rect= alien.get_rect()

#posicionar  Rectangulo del PLayer ###

#Posicion individual del rectangulo
player_rect.x= ancho/2
player_rect.y= largo-64
#Posicion del rectanulo
player_rect.center =((ancho/2,largo-64))

#Movimiento del player| Variable que almacena el valor de pixeles que se mueve el juagdor

player_x_change= 5


#Posicion Rectagulo del proyectil###

posicion_player = player_rect.x
#La bala siempre se va a ubicar donde este el jugador posicion_player y en largo-64
bullet_rect_x = posicion_player
bullet_rect_y =(largo-64)

#Activar proyectil

def is_collision(alien_x_random,alien_y_random,bullet_rect_x,bullet_rect_y):

    distancia = math.sqrt((alien_x_random-bullet_rect_x)**2 + (alien_y_random,bullet_rect_y)**2)

    #Valor de la distancia comparada en el if, es un valor arbitrario
    if distancia<27:
        return True
    else:
        return False
    

#Mostrar varios alienigenas
"""for i in range(nuemro_de_enemigos):
    alien.append(pygame.image.load("alien33.png"))
    alien_x_random.append(random.randint(0,ancho))
    alien_y_random.append(random.randint(50,150))
    alien_y_change.append(40)
    alien_x_change.append(5)
"""

running = True

while running:

    #Poner el fondo aca o no se va a mostar la bala
    pantalla.blit(fondo,(0,0))
    #Aqui muevo el rectangulo, si coloco alien_rect.x no se va a mover porque la posicion x
    #del alien en .blit es alien_x_random en lugar de alien_rect.x

    #Si lo coloco asi no se mueve pero no es lo correcto
    alien_x_random -= alien_x_change

    #Si lo coloco asi, si se mueve pero no es lo correcto a futuro
    #alien_x_random += alien_x_change

    #Limite de movimeinto del alien

    if alien_x_random<=0:

        alien_x_change *= -1
        alien_y_random += alien_y_change


    elif alien_x_random>= ancho:

        alien_x_change *= -1
        alien_y_random += alien_y_change
    
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        #Disparo de la bala####>>>>>

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if bullet_state == "ready":
                    print("hola")
                    bullet_rect_x = player_rect.x
                    bullet_state= "fire"


    #Movimiento del player

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left>= 0:
        player_rect.x -= player_x_change

    if keys[pygame.K_RIGHT] and player_rect.right<=ancho:
        player_rect.x += player_x_change


    #Si presiinamos el boton de disparo

    if bullet_state == "fire":
        
        pantalla.blit(bullet,(bullet_rect_x,bullet_rect_y))
        bullet_rect_y -= bullet_y_change 

    if bullet_rect_y <= 0:

        bullet_rect_y= (largo-64)
        bullet_state= "ready"

    #Pegar en pantalla los sprites

    
    pantalla.blit(player,player_rect)
    pantalla.blit(alien,(alien_x_random,alien_y_random))



    pygame.display.update()

    reloj.tick(FPS)