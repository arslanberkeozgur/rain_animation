import pygame
import random


WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Raining')

BG = pygame.transform.scale(pygame.image.load('cloudy-night.png'), (WIDTH, HEIGHT))


class Rain:
    def __init__(self,x, y, z, vx, vy):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx * z
        self.vy = vy * z

    def draw(self):
        pygame.draw.rect(WIN, (100,100,130), (self.x,self.y, 2*self.z, 20*self.z))

    def fall(self):
        ay = 0.04
        self.vy += ay
        self.x += self.vx
        self.y += self.vy


droplets = []



def main():
    run = True
    FPS = 120
    clock = pygame.time.Clock()



    def draw():
        WIN.blit(BG, (0,0))

        for rain in droplets:
            rain.draw()

        pygame.display.update()


    while run:
        clock.tick(FPS)

        draw()

        while len(droplets) < 500:
            droplet = Rain(random.randrange(0, WIDTH + 200), random.randrange(-2000, 0), random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]),-1,3)
            droplets.append(droplet)

        for droplet in droplets:
            droplet.fall()
            if droplet.y > HEIGHT:
                droplets.remove(droplet)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

main()