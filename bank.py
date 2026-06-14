# -------- 1. ЧИСТЫЕ ФУНКЦИИ (без input, print, побочных эффектов) --------

def calculate_deposit(balance: float, amount: float):
    """
    Чистая функция пополнения.
    Возвращает (новый_баланс, сообщение_об_ошибке).
    Если amount > 0, ошибка None.
    """
    if amount <= 0:
        return balance, "Сумма должна быть положительной."
    return balance + amount, None

def calculate_purchase(balance: float, amount: float, name: str):
    """
    Чистая функция покупки.
    Возвращает (новый_баланс, транзакция, сообщение_об_ошибке).
    Если всё ок, ошибка None, транзакция = {'name': ..., 'amount': ...}.
    """
    if amount <= 0:
        return balance, None, "Сумма должна быть положительной."
    if amount > balance:
        return balance, None, f"Недостаточно средств. Ваш баланс: {balance}"
    new_balance = balance - amount
    transaction = {'name': name, 'amount': amount}
    return new_balance, transaction, None

def add_transaction_to_history(history: list, transaction: dict):
    """
    Чистая функция: возвращает НОВЫЙ список истории.
    Не изменяет исходный.
    """
    if transaction is None:
        return history
    return history + [transaction]

def format_transaction(transaction: dict) -> str:
    """Чистая функция: форматирует транзакцию для вывода."""
    return f'{transaction["name"]} — {transaction["amount"]}'

# -------- 2. ГРЯЗНЫЕ ФУНКЦИИ (только ввод/вывод) --------

def deposit_interactive(balance: float) -> float:
    """Грязная обёртка: запрашивает сумму, вызывает чистую логику."""
    while True:
        try:
            amount = float(input('Введите сумму пополнения: '))
            new_balance, error = calculate_deposit(balance, amount)
            if error:
                print(error)
                continue
            print(f'Баланс пополнен, текущий баланс: {new_balance}')
            return new_balance
        except ValueError:
            print('Ошибка, введите число')

def buy_interactive(balance: float, history: list):
    """Грязная обёртка: запрашивает сумму и название, вызывает чистую логику."""
    while True:
        try:
            amount = float(input('Введите сумму покупки: '))
            if amount <= 0:
                print('Сумма должна быть положительной.')
                continue
            if amount > balance:
                print(f'Недостаточно средств. Ваш баланс: {balance}')
                return balance, history
            name = input('Введите название покупки: ')
            new_balance, transaction, error = calculate_purchase(balance, amount, name)
            if error:
                print(error)
                return balance, history
            new_history = add_transaction_to_history(history, transaction)
            print(f'Покупка "{name}" на сумму {amount} выполнена. Текущий баланс: {new_balance}')
            return new_balance, new_history
        except ValueError:
            print('Ошибка, введите число')

# -------- 3. ОСНОВНАЯ ФУНКЦИЯ run() --------

def run():
    balance = 0.0
    history = []

    print("\n--- МОЙ БАНКОВСКИЙ СЧЁТ ---")
    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Проверить баланс')
        print('5. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = deposit_interactive(balance)
        elif choice == '2':
            balance, history = buy_interactive(balance, history)
        elif choice == '3':
            if not history:
                print('История покупок пуста.')
            else:
                print('История покупок:')
                for i, item in enumerate(history, 1):
                    print(f'  {i}. {format_transaction(item)}')
        elif choice == '4':
            print(f'Ваш текущий баланс: {balance}')
        elif choice == '5':
            break
        else:
            print('Неверный пункт меню.')