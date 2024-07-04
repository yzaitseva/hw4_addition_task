# Функція для перевірки існування файлу
def file_exists(filepath):
    try:
        with open(filepath, 'r'):
            return True
    except FileNotFoundError:
        print(f"File {filepath} does not exist.")
        return False

# Функція що приймає 2 параметри — номер персонажа і попередній рядок
def get_validated_input(character_num, previous_line):
    print(f"Character {character_num} previous line: {previous_line}")
    user_input = input(f"Enter a new line for character {character_num} (at least 3 words): ")
    while len(user_input.split()) < 3:
        user_input = input("Please enter at least 3 words: ")
    return user_input

# Шляхи до файлів
file1_path = 'chapter1.txt'
file2_path = 'chapter2.txt'

# Перевірка існування файлів. Якщо хоч один з файлів не існує, програма завершується
if not file_exists(file1_path) or not file_exists(file2_path):
    exit()

# Зчитування вмісту файлів і збереження його у відповідні змінні lines1 і lines2
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

# Створення пустого списку для збереження сценарію
script_content = []

# Визначення кількості ітерацій. Повертає максимальну кількість рядків між двома файлами
max_len = max(len(lines1), len(lines2))

# Проходження по кожному рядку з файлів і перевірка
for i in range(max_len):
    if i < len(lines1):
        line1 = lines1[i].strip()
        if line1 == '$$$':
            previous_line = lines1[i - 1].strip() if i > 0 else 'None'
            user_input = get_validated_input(1, previous_line)
            script_content.append(user_input)
        else:
            script_content.append(line1)

    if i < len(lines2):
        line2 = lines2[i].strip()
        if line2 == '$$$':
            previous_line = lines2[i - 1].strip() if i > 0 else 'None'
            user_input = get_validated_input(2, previous_line)
            script_content.append(user_input)
        else:
            script_content.append(line2)

# Записування вмісту у файл script.txt, проходження через кожен рядок у списку
with open('script.txt', 'w') as script_file:
    for line in script_content:
        script_file.write(line + '\n')

print("The script is ready and saved in script.txt")
