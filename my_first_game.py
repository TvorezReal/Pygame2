import pygame
import random
import sys

pygame.init()
# Основные настройки экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# Настройки игрока
PLAYER_SIZE = 40
PLAYER_COLOR = (0, 255, 0)
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT-2*PLAYER_SIZE]

# Настройки врагов
ENEMY_SIZE = 40
ENEMY_COLOR = (255, 0, 0)
enemy_speed = 10
ENEMY_SPAWN_RATE = 30
enemies = []

class Player:
    def __init__(self):
        self.rect = pygame.Rect(player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE)

    def draw(self):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)

    def move(self, x, y):
        # Предварительное изменение координат
        new_x = self.rect.x + x
        new_y = self.rect.y + y

        # Проверка, не выходит ли игрок за пределы экрана
        # Если выходит, меняем положение, чтобы оно соответствовало границам
        if new_x < 0:
            new_x = 0
        elif new_x + PLAYER_SIZE > SCREEN_WIDTH:
            new_x = SCREEN_WIDTH - PLAYER_SIZE

        if new_y < 0:
            new_y = 0
        elif new_y + PLAYER_SIZE > SCREEN_HEIGHT:
            new_y = SCREEN_HEIGHT - PLAYER_SIZE

        # Обновляем положение игрока с учетом границ
        self.rect.x = new_x
        self.rect.y = new_y

class Enemy:
    def __init__(self):
        x = random.randint(0, SCREEN_WIDTH-ENEMY_SIZE)
        y = random.randint(0, SCREEN_HEIGHT-ENEMY_SIZE)
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.speed_x = random.choice([-enemy_speed, enemy_speed])
        self.speed_y = random.choice([-enemy_speed, enemy_speed])

    def draw(self):
        pygame.draw.rect(screen, ENEMY_COLOR, self.rect)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

player = Player()

def add_enemy():
    if len(enemies) < 10:
        enemies.append(Enemy())

def game_over():
    pygame.quit()
    sys.exit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move(-10, 0)
    if keys[pygame.K_RIGHT]:
        player.move(10, 0)
    if keys[pygame.K_UP]:
        player.move(0, -10)
    if keys[pygame.K_DOWN]:
        player.move(0, 10)

    screen.fill(BG_COLOR)

    if random.randint(1, ENEMY_SPAWN_RATE) == 1:
        add_enemy()

    for enemy in enemies:
        enemy.move()
        enemy.draw()
        if player.rect.colliderect(enemy.rect):
            print("Вы задели врага! - игра окончена!")
            game_over()

    player.draw()

    pygame.display.flip()
    clock.tick(20)  # FPS