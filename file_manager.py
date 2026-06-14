# file_manager.py (рефакторинг)

import os
import shutil
import platform

# Глобальная переменная (состояние) – оставляем, но доступ к ней только через грязные функции
_work_dir = os.getcwd()

def get_work_dir():
    return _work_dir

# ---------- 1. ЧИСТЫЕ ФУНКЦИИ (без ввода/вывода и побочных эффектов) ----------

def validate_folder_name(name: str) -> tuple:
    """
    Проверяет имя папки.
    Возвращает (is_valid, error_message).
    """
    if not name or not name.strip():
        return False, "Имя папки не может быть пустым."
    return True, None

def get_new_folder_path(base_dir: str, name: str, exists: bool) -> tuple:
    """
    Чистая функция: формирует путь и проверяет, можно ли создать.
    exists – заранее вычисленный флаг (os.path.exists(path) из обёртки).
    Возвращает (path, error_message).
    """
    path = os.path.join(base_dir, name)
    if exists:
        return None, f"Папка '{name}' уже существует."
    return path, None

def get_deletion_path(base_dir: str, name: str, exists: bool, is_dir: bool) -> tuple:
    """
    Чистая функция для удаления.
    Возвращает (path, error_message, is_dir_flag).
    """
    path = os.path.join(base_dir, name)
    if not exists:
        return None, f"'{name}' не найден.", False
    return path, None, is_dir

def get_copy_paths(base_dir: str, src_name: str, dst_name: str,
                   src_exists: bool, dst_exists: bool, src_is_dir: bool) -> tuple:
    """
    Чистая функция для копирования.
    Возвращает (src_path, dst_path, error_message, src_is_dir).
    """
    src = os.path.join(base_dir, src_name)
    dst = os.path.join(base_dir, dst_name)
    if not src_exists:
        return None, None, f"'{src_name}' не найден.", False
    if dst_exists:
        return None, None, f"'{dst_name}' уже существует.", False
    return src, dst, None, src_is_dir

def filter_items(items: list, filter_type: str) -> list:
    """
    Чистая функция: фильтрует список имён по типу.
    filter_type: 'dir' или 'file'.
    Принимает готовый список имён и функцию определения типа (должна быть передана извне? Нет, в чистой функции нельзя вызывать os.path.isdir.
    Поэтому для чистоты этот фильтр должен работать с предварительно размеченными данными.
    Упростим: пусть эта функция просто отбирает элементы, у которых есть метка типа.
    Лучше передавать список кортежей (name, is_dir).
    """
    if filter_type == 'dir':
        return [name for name, is_dir in items if is_dir]
    elif filter_type == 'file':
        return [name for name, is_dir in items if not is_dir]
    else:
        return [name for name, _ in items]

def format_os_info(os_data: dict) -> list:
    """
    Чистая функция: принимает словарь с данными об ОС, возвращает список строк для вывода.
    """
    return [
        f"Система:   {os_data['system']}",
        f"Версия:    {os_data['version']}",
        f"Машина:    {os_data['machine']}",
        f"Процессор: {os_data['processor']}"
    ]

# ---------- 2. ГРЯЗНЫЕ ФУНКЦИИ (ввод/вывод, работа с диском, глобальная переменная) ----------

def create_folder():
    name = input('Введите название папки: ').strip()
    valid, err = validate_folder_name(name)
    if not valid:
        print(err)
        return
    path = os.path.join(_work_dir, name)
    exists = os.path.exists(path)
    path, err = get_new_folder_path(_work_dir, name, exists)
    if err:
        print(err)
        return
    os.mkdir(path)
    print(f'Папка "{name}" создана.')

def delete():
    name = input('Введите название файла или папки для удаления: ').strip()
    path = os.path.join(_work_dir, name)
    exists = os.path.exists(path)
    is_dir = os.path.isdir(path) if exists else False
    path, err, is_dir_flag = get_deletion_path(_work_dir, name, exists, is_dir)
    if err:
        print(err)
        return
    if is_dir_flag:
        shutil.rmtree(path)
        print(f'Папка "{name}" удалена.')
    else:
        os.remove(path)
        print(f'Файл "{name}" удалён.')

def copy():
    src_name = input('Введите название файла/папки для копирования: ').strip()
    dst_name = input('Введите новое название: ').strip()
    src_path = os.path.join(_work_dir, src_name)
    dst_path = os.path.join(_work_dir, dst_name)
    src_exists = os.path.exists(src_path)
    dst_exists = os.path.exists(dst_path)
    src_is_dir = os.path.isdir(src_path) if src_exists else False
    src, dst, err, is_dir_flag = get_copy_paths(_work_dir, src_name, dst_name,
                                                src_exists, dst_exists, src_is_dir)
    if err:
        print(err)
        return
    if is_dir_flag:
        shutil.copytree(src, dst)
        print(f'Папка скопирована как "{dst_name}".')
    else:
        shutil.copy2(src, dst)
        print(f'Файл скопирован как "{dst_name}".')

def show_all():
    try:
        items = os.listdir(_work_dir)
    except OSError as e:
        print(f"Ошибка чтения директории: {e}")
        return
    if not items:
        print('Директория пуста.')
    else:
        print(f'\nСодержимое {_work_dir}:')
        for item in items:
            print(f'  {item}')

def show_folders():
    try:
        items = os.listdir(_work_dir)
    except OSError as e:
        print(f"Ошибка чтения директории: {e}")
        return
    # Собираем размеченные элементы (имя, is_dir)
    labeled = [(i, os.path.isdir(os.path.join(_work_dir, i))) for i in items]
    folders = filter_items(labeled, 'dir')
    if not folders:
        print('Папок нет.')
    else:
        print(f'\nПапки в {_work_dir}:')
        for item in folders:
            print(f'  📁 {item}')

def show_files():
    try:
        items = os.listdir(_work_dir)
    except OSError as e:
        print(f"Ошибка чтения директории: {e}")
        return
    labeled = [(i, os.path.isdir(os.path.join(_work_dir, i))) for i in items]
    files = filter_items(labeled, 'file')
    if not files:
        print('Файлов нет.')
    else:
        print(f'\nФайлы в {_work_dir}:')
        for item in files:
            print(f'  📄 {item}')

def show_os_info():
    os_data = {
        'system': platform.system(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor()
    }
    lines = format_os_info(os_data)
    print('\n--- Информация об ОС ---')
    for line in lines:
        print(line)

def change_dir():
    global _work_dir
    new_dir = input('Введите путь к новой рабочей директории: ').strip()
    if os.path.isdir(new_dir):
        _work_dir = new_dir
        print(f'Рабочая директория изменена: {_work_dir}')
    else:
        print('Такой директории не существует.')