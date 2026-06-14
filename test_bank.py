import pytest
from bank import (
    calculate_deposit,
    calculate_purchase,
    add_transaction_to_history,
    format_transaction
)


# ===== Тесты чистых функций =====

def test_calculate_deposit():
    new_bal, err = calculate_deposit(100, 50)
    assert new_bal == 150
    assert err is None

    new_bal, err = calculate_deposit(100, -10)
    assert new_bal == 100
    assert err == "Сумма должна быть положительной."

    new_bal, err = calculate_deposit(100, 0)
    assert new_bal == 100
    assert err == "Сумма должна быть положительной."


def test_calculate_purchase():
    # Успешная покупка
    new_bal, tx, err = calculate_purchase(100, 30, "хлеб")
    assert new_bal == 70
    assert tx == {'name': 'хлеб', 'amount': 30}
    assert err is None

    # Недостаточно средств
    new_bal, tx, err = calculate_purchase(50, 100, "телефон")
    assert new_bal == 50
    assert tx is None
    assert err == "Недостаточно средств. Ваш баланс: 50"

    # Отрицательная сумма
    new_bal, tx, err = calculate_purchase(100, -20, "что-то")
    assert new_bal == 100
    assert tx is None
    assert err == "Сумма должна быть положительной."


def test_add_transaction_to_history():
    old_history = [{'name': 'молоко', 'amount': 50}]
    new_tx = {'name': 'кофе', 'amount': 30}

    new_history = add_transaction_to_history(old_history, new_tx)
    assert new_history == [{'name': 'молоко', 'amount': 50}, {'name': 'кофе', 'amount': 30}]
    assert old_history == [{'name': 'молоко', 'amount': 50}]  # неизменность

    # Добавление None не меняет историю
    new_history = add_transaction_to_history(old_history, None)
    assert new_history == old_history


def test_format_transaction():
    tx = {'name': 'пицца', 'amount': 500}
    assert format_transaction(tx) == 'пицца — 500'