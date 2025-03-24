import pygame
import time
import random

# Alustetaan pygame
pygame.init()

# Värit
valkoinen = (255, 255, 255)
musta = (0, 0, 0)
punainen = (213, 50, 80)
vihreä = (0, 255, 0)

# Näytön koko
leveys = 600
korkeus = 400
näyttö = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('Matopeli')

# Maton koko
madon_koko = 10
nopeus = 15
kello = pygame.time.Clock()

fontti = pygame.font.SysFont("arial", 25)

def pisteet(pisteet):
    arvo = fontti.render("Pisteet: " + str(pisteet), True, vihreä)
    näyttö.blit(arvo, [0, 0])

def madon_pituus(mato_lista):
    for x in mato_lista:
        pygame.draw.rect(näyttö, musta, [x[0], x[1], madon_koko, madon_koko])

def peli():
    peli_käynnissä = True
    peli_loppu = False

    x = leveys / 2
    y = korkeus / 2

    x_muutos = 0
    y_muutos = 0

    mato_lista = []
    pituus = 1

    ruoka_x = round(random.randrange(0, leveys - madon_koko) / 10.0) * 10.0
    ruoka_y = round(random.randrange(0, korkeus - madon_koko) / 10.0) * 10.0

    while peli_käynnissä:

        while peli_loppu:
            näyttö.fill(valkoinen)
            viesti = fontti.render("Hävisit! Enter jatkaa, Q lopettaa", True, punainen)
            näyttö.blit(viesti, [leveys / 6, korkeus / 3])
            pisteet(pituus - 1)
            pygame.display.update()

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_q:
                        peli_käynnissä = False
                        peli_loppu = False
                    if tapahtuma.key == pygame.K_RETURN:
                        peli()

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                peli_käynnissä = False
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    x_muutos = -madon_koko
                    y_muutos = 0
                elif tapahtuma.key == pygame.K_RIGHT:
                    x_muutos = madon_koko
                    y_muutos = 0
                elif tapahtuma.key == pygame.K_UP:
                    y_muutos = -madon_koko
                    x_muutos = 0
                elif tapahtuma.key == pygame.K_DOWN:
                    y_muutos = madon_koko
                    x_muutos = 0

        x += x_muutos
        y += y_muutos

        if x >= leveys or x < 0 or y >= korkeus or y < 0:
            peli_loppu = True

        näyttö.fill(valkoinen)
        pygame.draw.rect(näyttö, punainen, [ruoka_x, ruoka_y, madon_koko, madon_koko])

        matopää = []
        matopää.append(x)
        matopää.append(y)
        mato_lista.append(matopää)

        if len(mato_lista) > pituus:
            del mato_lista[0]

        for segmentti in mato_lista[:-1]:
            if segmentti == matopää:
                peli_loppu = True

        madon_pituus(mato_lista)
        pisteet(pituus - 1)

        pygame.display.update()

        if x == ruoka_x and y == ruoka_y:
            ruoka_x = round(random.randrange(0, leveys - madon_koko) / 10.0) * 10.0
            ruoka_y = round(random.randrange(0, korkeus - madon_koko) / 10.0) * 10.0
            pituus += 1

        kello.tick(nopeus)

    pygame.quit()
    quit()

peli() 
