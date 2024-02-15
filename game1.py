import pygame
import time
import random
from IPython.display import display, Image
from PIL import Image as PILImage

WIDTH, HEIGHT = 1100, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

image_path = "file:///C:/Users/LENOVO/Downloads/pexels-felix-mittermeier-956981.jpg"
image = PILImage.open(image_path)
BG = display(Image(filename=image_path))

def draw():
    WIN.blit(BG,())

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

    pygame.quit()
if __name__=='__main__':
    main()
    

