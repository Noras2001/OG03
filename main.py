import pygame
import random

pygame.init()

# constants part
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("images/icono.jpg")
pygame.display.set_icon(icon)

target = pygame.image.load("images/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# рандомное значение заливки фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Скорость движения таргета по осям x и y
speed_x = random.randint(-5, 5)
speed_y = random.randint(-5, 5)

# переменные для мерцания
hit = False
flash_timer = 0
flash_duration = 500  # длительность мерцания в миллисекундах
flash_interval = 100  # интервал мерцания

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hit = True
                flash_timer = pygame.time.get_ticks()

    # логика мерцания
    current_time = pygame.time.get_ticks()
    if hit:
        if (current_time - flash_timer) < flash_duration:
            # меняем отображение каждые flash_interval миллисекунд
            if (current_time // flash_interval) % 2 == 0:
                screen.blit(target, (target_x, target_y))
        else:
            hit = False  # сбрасываем флаг после завершения мерцания
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    else:
        screen.blit(target, (target_x, target_y))

    pygame.display.update()

pygame.quit()