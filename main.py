import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    run = true
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
     
             run = false
    pygame.quit()
if __name__ == "__main__":
    main()                 