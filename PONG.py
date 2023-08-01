import pygame
from pygame import*
import sys
from paddle import Paddle

def main():
    pygame.init()
    black = (0,0,0)
    white = (255,255,255)
    size = (800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
    screen.fill(black)
    clock = pygame.time.Clock()
    sprite_list = pygame.sprite.Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.draw.line(screen, white, [400, 0], [400, 600], 5)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()