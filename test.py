import math
import random
import colorama

random.seed(1)

def draw_planet(radius=5):
    symbols = {
        1: f'{colorama.Fore.YELLOW}█{colorama.Fore.RESET}',  # поверхня
        2: f'{colorama.Fore.LIGHTYELLOW_EX}█{colorama.Fore.RESET}',  # вода
        3: f'{colorama.Fore.LIGHTBLACK_EX}█{colorama.Fore.RESET}'   # гори
    }

    for y in range(-radius, radius + 1):
        for x in range(-radius * 2, radius * 2 + 1):
            # Перевірка, чи точка знаходиться в колі
            distance = math.sqrt((x / 2) ** 2 + y ** 2)
            if distance <= radius:
                terrain = random.choices([1, 2, 3], weights=[50, 30, 20])[0]
                print(symbols[terrain], end='')
            else:
                print(' ', end='')
        print()

# Виклик функції
draw_planet(5)