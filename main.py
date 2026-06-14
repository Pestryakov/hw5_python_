import file_manager
import quiz
import bank

AUTHOR_INFO = {
    'name': 'Максим Пестряков',
    'role': 'Python-разработчик',
    'contact': 'pestriakovm@gmail.com',
}

def show_author() -> None:
    """Выводит информацию об авторе программы."""
    print(f'\n--- Создатель программы ---')
    print(f'Имя:      {AUTHOR_INFO["name"]}')
    print(f'Роль:     {AUTHOR_INFO["role"]}')
    print(f'Контакт:  {AUTHOR_INFO["contact"]}')

def show_menu() -> None:
    """Отображает главное меню программы."""
    print(f'\n=== КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР ===')
    print(f'Рабочая директория: {file_manager.get_work_dir()}')
    print('-------------------------------------')
    print('1.  Создать папку')
    print('2.  Удалить файл/папку')
    print('3.  Копировать файл/папку')
    print('4.  Просмотр содержимого директории')
    print('5.  Только папки')
    print('6.  Только файлы')
    print('7.  Информация об ОС')
    print('8.  Создатель программы')
    print('9.  Играть в викторину')
    print('10. Мой банковский счёт')
    print('11. Сменить рабочую директорию')
    print('0.  Выход')
    print('-------------------------------------')

def main() -> None:
    """Основной цикл программы."""
    # Словарь команд (без пунктов 0 и 8)
    commands = {
        '1': file_manager.create_folder,
        '2': file_manager.delete,
        '3': file_manager.copy,
        '4': file_manager.show_all,
        '5': file_manager.show_folders,
        '6': file_manager.show_files,
        '7': file_manager.show_os_info,
        '9': quiz.run,
        '10': bank.run,
        '11': file_manager.change_dir,
    }

    while True:
        show_menu()
        choice = input('Выберите пункт: ').strip()

        if choice == '0':
            print('До свидания!')
            break
        elif choice == '8':
            show_author()
        elif choice in commands:
            commands[choice]()
        else:
            print('Неверный пункт, попробуйте снова.')

if __name__ == '__main__':
    main()