import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rocket saga")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
VEL = 5
BULLETS_VEL = 7
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)
red_bullets = []
yellow_bullets = []
MAX_BULLETS =  10

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()
def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x-VEL > 0:
        red.x -= VEL
    if keys_pressed[pygame.K_d]and red.x+VEL+red.width < BORDER.x:   
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y-VEL > 0:   
        red.y -= VEL         
    if keys_pressed[pygame.K_s] and red.y+VEL+red.height < HEIGHT:   
        red.y += VEL
def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x-VEL > BORDER.x:
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x+VEL+yellow.width < WIDTH:   
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y-VEL > 0:   
        yellow.y -= VEL         
    if keys_pressed[pygame.K_DOWN]and yellow.y+VEL+yellow.height < HEIGHT:   
        yellow.y += VEL
def handle_bullets(yellow_bullets, red_bullets, red, yellow):
                          
def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow =pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
  

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(red.x + red.width, red.y + red.height/2, 10, 5 )
                red_bullets.append(bullet)

            if event.ket == pygame.k_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(yellow.x, yellow.y + yellow.height/2, 10, 5 )
                yellow_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed, red)
        yellow_movement(keys_pressed, yellow) 

        handle_bullets(yellow_bullets, red_bullets, yellow, red)




        draw_window(red ,yellow)   
    pygame.quit()
if __name__ == "__main__":
    main()                 