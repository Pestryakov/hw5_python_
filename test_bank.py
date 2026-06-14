from bank import run  # предполагаем, что bank.py в той же директории


def test_deposit_and_balance(monkeypatch, capsys):
    # Симулируем ввод: пополнение 100, затем проверка баланса, затем выход
    inputs = iter(["1", "100", "4", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Баланс пополнен, текущий баланс: 100.0" in captured.out
    assert "Ваш текущий баланс: 100.0" in captured.out


def test_purchase_success(monkeypatch, capsys):
    # Пополнение 100, покупка "кофе" за 50, выход
    inputs = iter(["1", "100", "2", "50", "кофе", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert 'Покупка "кофе" на сумму 50.0 выполнена' in captured.out
    assert "Текущий баланс: 50.0" in captured.out


def test_purchase_insufficient_funds(monkeypatch, capsys):
    # Пополнение 50, попытка купить за 100 (не хватает)
    inputs = iter(["1", "50", "2", "100", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Недостаточно средств. Ваш баланс: 50.0" in captured.out


def test_purchase_negative_amount(monkeypatch, capsys):
    # Пополнение 100, попытка ввести отрицательную сумму покупки, затем корректную
    inputs = iter(["1", "100", "2", "-50", "30", "книга", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Сумма должна быть положительной" in captured.out
    assert 'Покупка "книга" на сумму 30.0 выполнена' in captured.out


def test_deposit_negative_amount(monkeypatch, capsys):
    # Попытка пополнить на отрицательную сумму, затем на 200
    inputs = iter(["1", "-100", "200", "4", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Сумма должна быть положительной" in captured.out
    assert "Баланс пополнен, текущий баланс: 200.0" in captured.out


def test_history_empty(monkeypatch, capsys):
    # Сразу смотрим историю (пустую), потом выход
    inputs = iter(["3", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "История покупок пуста" in captured.out


def test_history_with_purchases(monkeypatch, capsys):
    # Пополнение, две покупки, просмотр истории, выход
    inputs = iter([
        "1", "200",
        "2", "50", "хлеб",
        "2", "30", "молоко",
        "3",
        "5"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "История покупок:" in captured.out
    assert "хлеб — 50.0" in captured.out
    assert "молоко — 30.0" in captured.out


def test_invalid_menu_choice(monkeypatch, capsys):
    # Неверный пункт меню, затем выход
    inputs = iter(["99", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Неверный пункт меню" in captured.out


def test_balance_after_multiple_operations(monkeypatch, capsys):
    # Пополнение 1000, покупка 250, пополнение 300, покупка 50, проверка баланса
    inputs = iter([
        "1", "1000",
        "2", "250", "билет",
        "1", "300",
        "2", "50", "кофе",
        "4",
        "5"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Баланс пополнен, текущий баланс: 1000.0" in captured.out
    assert "Покупка \"билет\" на сумму 250.0 выполнена" in captured.out
    assert "Баланс пополнен, текущий баланс: 1050.0" in captured.out  # 1000-250=750+300=1050
    assert "Покупка \"кофе\" на сумму 50.0 выполнена" in captured.out
    assert "Ваш текущий баланс: 1000.0" in captured.out  # 1050-50=1000


def test_purchase_with_string_instead_of_number(monkeypatch, capsys):
    # Ввод не числа для суммы покупки, затем корректное число
    inputs = iter(["1", "100", "2", "abc", "20", "вода", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Ошибка, введите число" in captured.out
    assert 'Покупка "вода" на сумму 20.0 выполнена' in captured.out