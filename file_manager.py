import os
import shutil
import platform

# Рабочая директория — папка откуда запущена программа
work_dir = os.getcwd()


def get_work_dir():
    return work_dir


def create_folder():
    name = input('Введите название папки: ').strip()
    path = os.path.join(work_dir, name)
    if os.path.exists(path):
        print(f'Папка "{name}" уже существует.')
    else:
        os.mkdir(path)
        print(f'Папка "{name}" создана.')



def delete():
    name = input('Введите название файла или папки для удаления: ').strip()
    path = os.path.join(work_dir, name)
    if not os.path.exists(path):
        print(f'"{name}" не найден.')
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f'Папка "{name}" удалена.')
    else:
        os.remove(path)
        print(f'Файл "{name}" удалён.')


def copy():
    name = input('Введите название файла/папки для копирования: ').strip()
    new_name = input('Введите новое название: ').strip()
    src = os.path.join(work_dir, name)
    dst = os.path.join(work_dir, new_name)
    if not os.path.exists(src):
        print(f'"{name}" не найден.')
    elif os.path.exists(dst):
        print(f'"{new_name}" уже существует.')
    elif os.path.isdir(src):
        shutil.copytree(src, dst)
        print(f'Папка скопирована как "{new_name}".')
    else:
        shutil.copy2(src, dst)
        print(f'Файл скопирован как "{new_name}".')


def show_all():
    items = os.listdir(work_dir)
    if not items:
        print('Директория пуста.')
    else:
        print(f'\nСодержимое {work_dir}:')
        for item in items:
            print(f'  {item}')


def show_folders():
    items = [i for i in os.listdir(work_dir) if os.path.isdir(os.path.join(work_dir, i))]
    if not items:
        print('Папок нет.')
    else:
        print(f'\nПапки в {work_dir}:')
        for item in items:
            print(f'  📁 {item}')


def show_files():
    items = [i for i in os.listdir(work_dir) if os.path.isfile(os.path.join(work_dir, i))]
    if not items:
        print('Файлов нет.')
    else:
        print(f'\nФайлы в {work_dir}:')
        for item in items:
            print(f'  📄 {item}')


def show_os_info():
    print('\n--- Информация об ОС ---')
    print(f'Система:   {platform.system()}')
    print(f'Версия:    {platform.version()}')
    print(f'Машина:    {platform.machine()}')
    print(f'Процессор: {platform.processor()}')


def change_dir():
    global work_dir
    new_dir = input('Введите путь к новой рабочей директории: ').strip()
    if os.path.isdir(new_dir):
        work_dir = new_dir
        print(f'Рабочая директория изменена: {work_dir}')
    else:
        print('Такой директории не существует.')
