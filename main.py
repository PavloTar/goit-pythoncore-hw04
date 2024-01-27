import os

# ЗАВДАННЯ 1

# розробити функцію total_salary(path), яка аналізує файл  (/files/salary_file.txt) і повертає загальну та середню суму заробітної плати всіх розробників
def total_salary(path):
    total_salary = 0
    num_developers = 0
    if not os.path.isfile(path):
        print(f"Файл {path} не знайдений!")
        return None, None
    
    try:
        with open(path, 'r') as file:
            for line in file:
                try:
                    _, salary_str = line.split(',')
                    salary = int(salary_str)
                    total_salary += salary
                    num_developers += 1
                except ValueError:
                    print(f"Помилка при обробці рядка: {line}")

        if num_developers == 0:
            print("У файлі немає коректних записів про зарплату розробників.")
            return 0, 0  # Повертаємо 0 як загальну та середню зарплату, якщо немає коректних записів

        average_salary = total_salary / num_developers
        return total_salary, average_salary
    except Exception as e:
        print(f"Error: {e}")
        return None, None


# Приклад використання
print("\n================================ ЗАВДАННЯ 1 ======================================\n")

path_to_file = './files/salary_file.txt'
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# ЗАВДАННЯ 2

#розробити функцію get_cats_info(path), яка читає файл файл  (/files/cats_file.txt) та повертає список словників з інформацією про кожного кота.

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, cat_name, cat_age = line.strip().split(',')
                    cat_info = {"id": cat_id, "name": cat_name, "age": cat_age}
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Помилка при обробці рядка: {line}")
        return cats_info
    except FileNotFoundError:
        print(f"Файл {path} не знайдений!")
    except Exception as e:
        print(f"Error: {e}")

# Приклад використання
print("\n================================ ЗАВДАННЯ 2 ======================================\n")

path_to_cats_file = './files/cats_file.txt'
cats_info = get_cats_info(path_to_cats_file)

print(f"Список котів з файлу:\n {cats_info}")
   

#----------------------------------------------------------------------------------------------------------------------------------------------------------    


