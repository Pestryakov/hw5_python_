# test_file_manager.py

import pytest
from file_manager import (
    validate_folder_name,
    get_new_folder_path,
    get_deletion_path,
    get_copy_paths,
    filter_items,
    format_os_info
)

def test_validate_folder_name():
    valid, err = validate_folder_name("my_folder")
    assert valid is True
    assert err is None

    valid, err = validate_folder_name("")
    assert valid is False
    assert err == "Имя папки не может быть пустым."

    valid, err = validate_folder_name("   ")
    assert valid is False
    assert err == "Имя папки не может быть пустым."

def test_get_new_folder_path():
    # exists = False, папку можно создать
    path, err = get_new_folder_path("/tmp", "new", exists=False)
    assert path == "/tmp/new"
    assert err is None

    # exists = True, ошибка
    path, err = get_new_folder_path("/tmp", "existing", exists=True)
    assert path is None
    assert err == "Папка 'existing' уже существует."

def test_get_deletion_path():
    # существует и является папкой
    path, err, is_dir = get_deletion_path("/tmp", "dir", exists=True, is_dir=True)
    assert path == "/tmp/dir"
    assert err is None
    assert is_dir is True

    # не существует
    path, err, is_dir = get_deletion_path("/tmp", "missing", exists=False, is_dir=False)
    assert path is None
    assert err == "'missing' не найден."
    assert is_dir is False

def test_get_copy_paths():
    src_exists = True
    dst_exists = False
    src_is_dir = False
    src, dst, err, is_dir = get_copy_paths("/tmp", "file.txt", "copy.txt",
                                            src_exists, dst_exists, src_is_dir)
    assert src == "/tmp/file.txt"
    assert dst == "/tmp/copy.txt"
    assert err is None
    assert is_dir is False

    # источник не существует
    src, dst, err, is_dir = get_copy_paths("/tmp", "missing", "copy.txt",
                                            False, False, False)
    assert src is None
    assert err == "'missing' не найден."

    # цель существует
    src, dst, err, is_dir = get_copy_paths("/tmp", "file.txt", "copy.txt",
                                            True, True, False)
    assert err == "'copy.txt' уже существует."

def test_filter_items():
    labeled = [("a", True), ("b", False), ("c", True), ("d", False)]
    dirs = filter_items(labeled, "dir")
    assert dirs == ["a", "c"]

    files = filter_items(labeled, "file")
    assert files == ["b", "d"]

def test_format_os_info():
    data = {
        'system': 'Linux',
        'version': '5.4.0',
        'machine': 'x86_64',
        'processor': 'Intel'
    }
    lines = format_os_info(data)
    assert lines[0] == "Система:   Linux"
    assert lines[1] == "Версия:    5.4.0"
    assert lines[2] == "Машина:    x86_64"
    assert lines[3] == "Процессор: Intel"