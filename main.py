import file_manager
import quiz
import bank

AUTHOR = {
    'name': 'Максим Пестряков',
    'role': 'Python-разработчик',
    'contact': 'pestriakovm@gmail.com',
}

def show_menu():
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


def main():
    while True:
        show_menu()
        choice = input('Выберите пункт: ').strip()

        if choice == '1':
            file_manager.create_folder()
        elif choice == '2':
            file_manager.delete()
        elif choice == '3':
            file_manager.copy()
        elif choice == '4':
            file_manager.show_all()
        elif choice == '5':
            file_manager.show_folders()
        elif choice == '6':
            file_manager.show_files()
        elif choice == '7':
            file_manager.show_os_info()
        elif choice == '8':
            print(f'\n--- Создатель программы ---')
            print(f'Имя:      {AUTHOR["name"]}')
            print(f'Роль:     {AUTHOR["role"]}')
            print(f'Контакт:  {AUTHOR["contact"]}')
        elif choice == '9':
            quiz.run()
        elif choice == '10':
            bank.run()
        elif choice == '11':
            file_manager.change_dir()
        elif choice == '0':
            print('До свидания!')
            break
        else:
            print('Неверный пункт, попробуйте снова.')


if __name__ == '__main__':
    main()