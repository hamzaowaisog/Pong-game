import sys
import pygame
from paddle import Paddle
from ball import Ball

def display_winner(screen, font, player_name):
    text = font.render(f"{player_name} wins!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

def main():
    pygame.init()
    black = (0,0,0)
    white = (255,255,255)
    size = (800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    paddle1 = Paddle(white, 10, 100)
    paddle1.rect.x = 5
    paddle1.rect.y = 250

    paddle2 = Paddle(white, 10, 100)
    paddle2.rect.x = 785
    paddle2.rect.y = 250

    ball = Ball(white,20,20)
    ball.rect.x = 400
    ball.rect.y = 200

    sprites_list = pygame.sprite.Group()
    sprites_list.add(paddle1)
    sprites_list.add(paddle2)
    sprites_list.add(ball)

    score_1 = 0
    score_2 = 0
    scoring_sound = pygame.mixer.Sound("scoring.wav")
    poping_sound = pygame.mixer.Sound("poping.wav")
    game_started = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    sys.exit()
            if event.type == pygame.KEYUP and not game_started:
                game_started = True


        if game_started:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddle1.moveUp(10)
            if keys[pygame.K_s]:
                paddle1.moveDown(10)
            if keys[pygame.K_UP]:
                paddle2.moveUp(10)
            if keys[pygame.K_DOWN]:
                paddle2.moveDown(10)

            sprites_list.update()

            if ball.rect.x>=780:
                score_1 += 1
                scoring_sound.play()
                if score_1 >= 10:
                    display_winner(screen, font, "Player 1")
                    pygame.time.wait(1000)
                    score_1 = 0
                    score_2 = 0
                ball.velocity[0] = -ball.velocity[0]
                ball.rect.x = 400
                ball.rect.y = 200


            if ball.rect.x<=2:
                score_2 += 1
                scoring_sound.play()
                if score_2 >= 10:
                    display_winner(screen, font, "Player 2")
                    pygame.time.wait(1000)
                    score_1 = 0
                    score_2 = 0
                ball.velocity[0] = -ball.velocity[0]
                ball.rect.x = 400
                ball.rect.y = 200

            if ball.rect.y>580:
                ball.velocity[1] = -ball.velocity[1]

            if ball.rect.y<2:
                ball.velocity[1] = -ball.velocity[1]

            if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
                ball.bounce()
                poping_sound.play()
            screen.fill(black)
            pygame.draw.line(screen, white, [400, 0], [400, 600], 5)
            sprites_list.draw(screen)
            font = pygame.font.Font(None, 74)
            text = font.render(str(score_1), 1, white)
            screen.blit(text, (250,10))
            text = font.render(str(score_2), 1, white)
            screen.blit(text, (520,10))
        else:
            font = pygame.font.Font(None, 74)
            text = font.render("Press Up key to start", 1, white)
            screen.blit(text, (135, 300))

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()