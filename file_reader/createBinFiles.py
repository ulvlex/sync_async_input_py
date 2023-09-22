import os

# полный путь к каталогу, где должны быть созданы файлы
directory_path = "c:/binFiles"

# Проверяем, существует ли указанный каталог
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Создаем и заполняем 10 бинарных файлов
for i in range(1, 11):
    # Формируем имя файла, например: file1.bin, file2.bin, и т.д.
    file_name = f"file{i}.bin"

    # Полный путь к файлу
    file_path = os.path.join(directory_path, file_name)

    # Открываем файл для записи в бинарном режиме и заполняем его данными
    with open(file_path, "wb") as f:
        one_megabyte = 1024 * 1024
        data = b'\x00' * one_megabyte
        f.write(data)

    print(f"Бинарный файл {file_name} размером 1 Мегабайт создан: {file_path}")

print("Все файлы созданы.")
