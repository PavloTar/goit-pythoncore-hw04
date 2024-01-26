# ЗАВДАННЯ 4

# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.


# Ініціалізація словника для збереження контактів (ім'я -> телефон)
contacts = {}

# Функція для розбору введеного користувачем рядка
def parse_input(user_input):
    command_parts = user_input.lower().split()
    if not command_parts:
        return ("Invalid command",)
    
    command = command_parts[0]
    args = command_parts[1:]
    
    return (command, args)

# Функція для додавання контакту
def add_contact(name, phone):
    # Перевірка на правильність введених аргументів
    if not name or not phone:
        return "Invalid command. Usage: add [name] [phone]"
    
    contacts[name] = phone
    return "Contact added."

# Функція для зміни існуючого номера телефону контакту
def change_contact(name, phone):
    # Перевірка на правильність введених аргументів
    if not name or not phone:
        return "Invalid command. Usage: change [name] [phone]"
    
    # Перевірка чи існує контакт з введеним ім'ям
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# Функція для виведення номера телефону контакту
def show_phone(name):
    # Перевірка на правильність введеного аргументу
    if not name:
        return "Invalid command. Usage: phone [name]"
    
    # Перевірка чи існує контакт з введеним ім'ям
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# Функція для виведення всіх збережених контактів
def show_all():
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available."

# Основна функція для управління взаємодією з користувачем
def main():
    print("Welcome to the assistant bot!")
    print("How can I help you? Type 'help' for command information.")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        # Логіка обробки різних команд
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args[0], args[1]))
            else:
                print("Invalid command. Usage: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(args[0], args[1]))
            else:
                print("Invalid command. Usage: change [name] [phone]")
        elif command == "phone":
            if len(args) == 1:
                print(show_phone(args[0]))
            else:
                print("Invalid command. Usage: phone [name]")
        elif command == "all":
            print(show_all())
        elif command == "help":
            print("Available commands:")
            print("  - hello")
            print("  - add [name] [phone]")
            print("  - change [name] [phone]")
            print("  - phone [name]")
            print("  - all")
            print("  - close or exit")
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Type 'help' for command information.")

# Початок виконання програми, якщо цей файл запускається
if __name__ == "__main__":
    main()