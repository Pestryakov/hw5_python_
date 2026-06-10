def run():
    balance = 0
    history = []

    def deposit(x):
        while True:
            try:
                amount = float(input('Введите сумму пополнения: '))
                if amount > 0:
                    x += amount
                    print(f'Баланс пополнен, текущий баланс: {x}')
                    return x
                else:
                    print('Сумма должна быть положительной.')
            except ValueError:
                print('Ошибка, введите число')

    def buy(x):
        while True:
            try:
                amount = float(input('Введите сумму покупки: '))
                if amount <= 0:
                    print('Сумма должна быть положительной.')
                    continue
                if amount > x:
                    print(f'Недостаточно средств. Ваш баланс: {x}')
                    return x, history
                name = input('Введите название покупки: ')
                x -= amount
                history.append({'name': name, 'amount': amount})
                print(f'Покупка "{name}" на сумму {amount} выполнена. Текущий баланс: {x}')
                return x, history
            except ValueError:
                print('Ошибка, введите число')

    print("\n--- МОЙ БАНКОВСКИЙ СЧЁТ ---")
    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Проверить баланс')
        print('5. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance, history = buy(balance)
        elif choice == '3':
            if not history:
                print('История покупок пуста.')
            else:
                print('История покупок:')
                for i, item in enumerate(history, 1):
                    print(f'  {i}. {item["name"]} — {item["amount"]}')
        elif choice == '4':
            print(f'Ваш текущий баланс: {balance}')
        elif choice == '5':
            break
        else:
            print('Неверный пункт меню.')
