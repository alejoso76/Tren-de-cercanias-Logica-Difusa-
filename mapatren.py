import pygame
from prueba import *

ancho=1200
alto=800
centro=[300,300]

def proxi(posi, pos):
    return abs(pos-posi)

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    img=pygame.image.load('1.jpg')
    puerta=pygame.image.load('metro.png')
    puerta=pygame.transform.scale(puerta,(ancho,alto))

    Proximidad=[20, 100, 160, 240, 450]
    Caso=["Bicocca", "Cadorna", "Centrale","Palestro", "San Siro", "Stadio"]

    posi=0
    acc.input['v'] = 0
    vf.input['v'] = 0

    cont=30
    fuente=pygame.font.Font(None,48)
    fuente1=pygame.font.Font(None,48)
    fuente2=pygame.font.Font(None,48)
    reloj=pygame.time.Clock()
    fin=False
    pos=[0,0]


    #ciclo del programa
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        #Logica del ciclo
        if Proximidad != [] and cont<0:
            acc.input['x'] = proxi(posi, Proximidad[0])
                

        if pos[0]<=(-9000):
            pos[0]=0

        if cont<0:
            acc.compute()
            vf.input['a']=acc.output['af']
            vf.compute()
            if Proximidad!=[]:
                pos[0]= pos[0] - round(vf.output['vf'])
            acc.input['v'] = vf.output['vf']
            vf.input['v'] = vf.output['vf']
            posi+=1


        pantalla.blit(img,pos)
        pantalla.blit(puerta,[0,0])

        if Proximidad!=[] and cont<0:
            dista= "Distancia: "+str(proxi(posi, Proximidad[0]))+" Km"
            texto1=fuente.render(dista, 0, (255,230,245))
            velo= "Velocidad: "+str(round(vf.output['vf'] ))+" Km/h"
            texto=fuente.render(velo, 0, (255,230,245))
        else:
            texto1=fuente.render("Distancia: 0 Km", 0, (255,230,245))
            texto=fuente.render("Velocidad: 0 Km/h", 0, (255,230,245))

        if len(Caso) != 1:
            desti="anterior: "+Caso[0]+"   Sig: "+Caso[1]
            texto2=fuente.render(desti, 0, (255,230,245))
        else:
            desti="Fin del recorrido"
            texto2=fuente.render(desti, 0, (255,230,245))

        pantalla.blit(texto,[0,0])
        pantalla.blit(texto1,[0,48])
        pantalla.blit(texto2,[500,0])

        if Proximidad!=[]:
            if posi==Proximidad[0]:
                Proximidad.remove(posi)
                cont=30
                vf.input['v'] = 0
                acc.input['v'] = 0
                vf.input['a']= 0
                Caso.remove(Caso[0])

        #REfresco de pantalla
        reloj.tick(10)
        cont-=1
        pygame.display.flip()