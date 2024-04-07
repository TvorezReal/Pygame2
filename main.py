import pygame
import time

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image = pygame.image.load("dude.png")
image_rect = image.get_rect()
image2 = pygame.image.load("bottle.png")
image_rect2 = image.get_rect()

# speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            image_rect.center = event.pos
            mouse_x, mouse_y = event.pos
    if image_rect.colliderect(image_rect2):
        print("Встреча с бутылкой")
        time.sleep(1)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed
    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()