# ЗАВДАННЯ 3

# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів.
# Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

from colorama import Fore, init
from pathlib import Path
import sys

# Ініціалізуємо colorama та вказуємо autoreset=True для автоматичного скидання кольорів
init(autoreset=True)

def display_directory_structure(directory_path, indent=0):
  
    # indent - використовується для визначення відступу при виведенні ієрархічної структури каталогу в терміналі, вказує, на скільки пробілів або символів табуляції слід відступити перед виведенням кожного рівня вкладеності.

    try:
        # Створюємо об'єкт Path на основі вказаного шляху
        path = Path(directory_path)

        # Перевіряємо, чи шлях існує та є каталогом
        if not path.exists() or not path.is_dir():
            # Виводимо повідомлення про помилку, якщо шлях неправильний
            print(f"{Fore.RED}Error: The specified path is not a valid directory.")
            return

        # Проходимося по всім елементам каталогу
        for item in path.iterdir():
            if item.is_dir():
                # Виводимо директорії синім кольором та викликаємо рекурсивно для виведення їхньої структури ()
                print(f"{Fore.CYAN}{'  ' * indent}📁 {item.name}")
                display_directory_structure(item, indent + 1)
            else:
                # Виводимо файли зеленим кольором
                print(f"{Fore.GREEN}{'  ' * indent}📜 {item.name}")

    except Exception as e:
        # Виводимо повідомлення про будь-яку іншу помилку червоним кольором
        print(f"{Fore.RED}An error occurred: {e}")

if __name__ == "__main__":
    # Перевіряємо кількість переданих аргументів командного рядка
    if len(sys.argv) != 2:
        # Виводимо повідомлення про використання, якщо кількість аргументів неправильна
        print(f"{Fore.RED}Usage: python hw03.py /path/to/directory")
    else:
        # Викликаємо функцію display_directory_structure з переданим шляхом до каталогу
        directory_path = sys.argv[1]
        display_directory_structure(directory_path)