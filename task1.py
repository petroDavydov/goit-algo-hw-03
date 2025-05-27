import os
import shutil
import argparse

def copy_and_sort_files(source_directory, destination_directory):
    """
    Рекурсивно копіює файли, переміщує їх до нової директорії та сортує за розширенням.
    """
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)  # Якщо немає дерикторії -> створюємо

    for item in os.listdir(source_directory):
        item_path = os.path.join(source_directory, item)

        if os.path.isdir(item_path):
            copy_and_sort_files(item_path, destination_directory)  # Обробка піддиректорії
        else:
            try:
                file_extension = os.path.splitext(item)[1].lower()  # Розширення файлу
                extension_directory = os.path.join(destination_directory, file_extension[1:] or "unknown")  # Папка для розширення use hint

                if not os.path.exists(extension_directory):
                    os.makedirs(extension_directory)  # Створюємо папку для розширення

                shutil.copy2(item_path, extension_directory)  # Копіюємо файл у відповідну папку
                print(f"✅ Копіюємо '{item}' до '{extension_directory}'")

            except Exception as error:
                print(f"⚠️ Помилка копіювання '{item}': {error}")

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Рекурсивне копіювання/сортування файлів.")
    argument_parser.add_argument("source_directory", help="Шлях до вихідної директорії")
    argument_parser.add_argument("destination_directory", nargs="?", default="dist", help="Шлях до директорії в яку копіюємо (дефолтно 'dist')")

    arguments = argument_parser.parse_args()
    destination_directory = arguments.destination_directory if arguments.destination_directory else "dist"  # ✅ Використання "dist" як значення за замовчуванням

    if os.path.exists(arguments.source_directory):
        copy_and_sort_files(arguments.source_directory, destination_directory)
        print(f"🎉 Файли скопійовані та відсортовані в '{destination_directory}'!")
    else:
        print(f"❌ Директорія '{arguments.source_directory}' не існує!")

# Запуск програми:
# python task1.py <source_directory> <destination_directory>
# Запуск програми без параметрів:
# python task1.py <source_directory> -> буде використовуватися "dist" як директорія призначення