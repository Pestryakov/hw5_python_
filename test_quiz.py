import pytest
from quiz import (
    get_celebrities,
    is_correct,
    calculate_stats,
    should_play_again,
    ask_year,
    ask_play_again,
    display_stats,
    run
)


# ===== 1. Тесты для ЧИСТЫХ функций (без подмены input) =====

def test_get_celebrities():
    celebs = get_celebrities()
    assert len(celebs) == 5
    assert celebs[0]["name"] == "А.С. Пушкин"
    assert celebs[0]["year"] == 1799
    assert celebs[4]["name"] == "Леонардо да Винчи"
    assert celebs[4]["year"] == 1452


def test_is_correct():
    assert is_correct(1799, 1799) is True
    assert is_correct(1800, 1799) is False
    assert is_correct(0, 0) is True


def test_calculate_stats():
    stats = calculate_stats(3, 2, 5)
    assert stats["correct"] == 3
    assert stats["wrong"] == 2
    assert stats["percent_correct"] == 60.0
    assert stats["percent_wrong"] == 40.0


def test_calculate_stats_zero_total():
    stats = calculate_stats(0, 0, 0)
    assert stats["percent_correct"] == 0
    assert stats["percent_wrong"] == 0


def test_should_play_again():
    assert should_play_again("да") is True
    assert should_play_again("Да") is True
    assert should_play_again("  да  ") is True
    assert should_play_again("нет") is False
    assert should_play_again("НЕТ") is False


# ===== 2. Тесты для ГРЯЗНЫХ функций (с monkeypatch и capsys) =====

def test_ask_year_valid(monkeypatch, capsys):
    # Подменяем input: сначала "abc" (ошибка), потом "1799"
    inputs = iter(["abc", "1799"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = ask_year("Пушкин")

    captured = capsys.readouterr()
    assert "Пожалуйста, введите год числами!" in captured.out
    assert result == 1799


def test_ask_play_again_yes(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "да")
    result = ask_play_again()
    assert result is True


def test_ask_play_again_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "нет")
    result = ask_play_again()
    assert result is False


def test_ask_play_again_invalid_then_yes(monkeypatch, capsys):
    # Сначала "может", потом "да"
    inputs = iter(["может", "да"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = ask_play_again()

    captured = capsys.readouterr()
    assert "Пожалуйста, введите 'да' или 'нет'!" in captured.out
    assert result is True


def test_display_stats(capsys):
    stats = {"correct": 3, "wrong": 2, "percent_correct": 60.0, "percent_wrong": 40.0}
    display_stats(stats)
    captured = capsys.readouterr()
    assert "Количество правильных ответов: 3" in captured.out
    assert "Количество ошибок: 2" in captured.out
    assert "Процент правильных ответов: 60%" in captured.out
    assert "Процент неправильных ответов: 40%" in captured.out


# ===== 3. Сквозной тест для run (целиком) =====
def test_run_full(monkeypatch, capsys):
    # Симулируем полную игру: ответы на все вопросы, потом "нет"
    inputs = iter([
        "1799",  # Пушкин
        "1840",  # Чайковский
        "1934",  # Гагарин
        "1879",  # Эйнштейн
        "1452",  # Да Винчи
        "нет"  # не играть снова
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    captured = capsys.readouterr()
    assert "Правильно!" in captured.out
    assert "Правильных ответов: 5" in captured.out
    assert "Спасибо за игру!" in captured.out