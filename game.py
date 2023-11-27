import pygame
import random
import sys

from main import RegularCarComponentFactory, SportsCarComponentFactory, Car

# Использование фабрик и создание машин
regular_car_factory = RegularCarComponentFactory()
sports_car_factory = SportsCarComponentFactory()

a = input("Введите желаемую машину (1 - простая, 2 - гоночная): ")
while not(a in "1 2".split()):
    a = input("Введите желаемую машину (1 - простая, 2 - гоночная): ")
if int(a) == 1:
    car = Car(regular_car_factory)
else:
    car = Car(sports_car_factory)
print("Создана машина -", car, "класса", type(car))
print(car.get_description())

b = input("Не хотели бы прокатиться на ней (да/нет)? ")
while not(b in "да нет".split()):
    b = input("Не хотели бы прокатиться на ней (да/нет)? ")
if b == "нет":
    print("Ничего страшного! Спасибо за использование программы!")
    sys.exit()
print("Запущено окно игры!")

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размер экрана
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Супер Ралли")

# Загрузка изображения машинки
if int(a) == 1:
    # Скорость машинки
    car_speed = 5 / 1.6

    # Скорость прокрутки фона
    bg_speed = 2 / 1

    # Скорость предметов
    item_speed = 3 / 1

    car_img = pygame.image.load("car.png")
else:
    # Скорость машинки
    car_speed = 5 / 1.3

    # Скорость прокрутки фона
    bg_speed = 2 / 0.7

    # Скорость предметов
    item_speed = 3 / 0.7

    car_img = pygame.image.load("sportcar.png")
car_img = pygame.transform.scale(car_img, (50, 100))

# Загрузка фонового изображения
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Начальные координаты машинки
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 100

# Параметры предметов
item_width = 50
item_height = 50
item_x = random.randint(0, WIDTH - item_width)
item_y = 0


# Очки
score = 0

# Шрифт
font = pygame.font.Font(None, 36)

# Позиция фона
bg_y = 0

current_item = random.randint(0, 1)  # white = 1, red = 0
item_color = [RED, WHITE][current_item]

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= car_speed
    if keys[pygame.K_DOWN] and car_y < HEIGHT - 100:
        car_y += car_speed

    # Двигаем предмет вниз
    item_y += item_speed

    # Если предмет выходит за пределы экрана, создаем новый
    if item_y > HEIGHT:
        current_item = random.randint(0, 1)  # white = 1, red = 0
        item_color = [RED, WHITE][current_item]
        item_x = random.randint(130, WIDTH - item_width - 130)
        item_y = -100

    # Определяем коллизии между машинкой и предметом
    if car_x < item_x + item_width and car_x + 50 > item_x and car_y < item_y + item_height and car_y + 100 > item_y:
        if current_item == 1:
            score += 100
        else:
            score -= 50
        current_item = random.randint(0, 1)  # white = 1, red = 0
        item_color = [RED, WHITE][current_item]
        item_x = random.randint(130, WIDTH - item_width - 130)
        item_y = -100

    # Очки
    score_text = font.render("Очки: " + str(score), True, WHITE)

    # Прокрутка фона
    bg_y += bg_speed
    if bg_y >= HEIGHT:
        bg_y = 0

    # Отрисовка фона
    screen.blit(background_img, (0, bg_y))
    screen.blit(background_img, (0, bg_y - HEIGHT))

    # Отрисовка машинки
    screen.blit(car_img, (car_x, car_y))

    # Отрисовка предмета
    pygame.draw.rect(screen, item_color, (item_x, item_y, item_width, item_height))

    # Отрисовка текста с очками
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.update()

# Завершение игры
pygame.quit()
sys.exit()
