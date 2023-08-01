import sys

import pygame

from paddle import Paddle


def main():
    pygame.init()
    black = (0,0,0)
    white = (255,255,255)
    size = (800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    paddle1 = Paddle(white, 10, 100)
    paddle1.rect.x = 20
    paddle1.rect.y = 200

    paddle2 = Paddle(white, 10, 100)
    paddle2.rect.x = 770
    paddle2.rect.y = 200

    sprites_list = pygame.sprite.Group()
    sprites_list.add(paddle1)
    sprites_list.add(paddle2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.moveUp(5)
        if keys[pygame.K_s]:
            paddle1.moveDown(5)
        if keys[pygame.K_UP]:
            paddle2.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddle2.moveDown(5)

        sprites_list.update()
        screen.fill(black)
        pygame.draw.line(screen, white, [400, 0], [400, 600], 5)
        sprites_list.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()