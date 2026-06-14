# quiz.py (переработанный)

# -------- 1. ЧИСТЫЕ ФУНКЦИИ (без input, print, глобальных переменных) --------

def get_celebrities():
    """Возвращает список вопросов (можно легко заменить в тесте)."""
    return [
        {"name": "А.С. Пушкин", "year": 1799},
        {"name": "П.И. Чайковский", "year": 1840},
        {"name": "Юрий Гагарин", "year": 1934},
        {"name": "Альберт Эйнштейн", "year": 1879},
        {"name": "Леонардо да Винчи", "year": 1452},
    ]

def is_correct(user_year: int, correct_year: int) -> bool:
    """Проверяет ответ (чистая логика)."""
    return user_year == correct_year

def calculate_stats(correct: int, wrong: int, total: int) -> dict:
    """Возвращает статистику в виде словаря."""
    if total == 0:
        return {"correct": 0, "wrong": 0, "percent_correct": 0, "percent_wrong": 0}
    percent_correct = correct * 100 / total
    percent_wrong = wrong * 100 / total
    return {
        "correct": correct,
        "wrong": wrong,
        "percent_correct": percent_correct,
        "percent_wrong": percent_wrong,
    }

def should_play_again(answer: str) -> bool:
    """Чистое решение: да -> True, нет -> False."""
    return answer.lower().strip() == "да"

# -------- 2. ГРЯЗНЫЕ ФУНКЦИИ (только ввод/вывод, очень маленькие) --------

def ask_year(person_name: str) -> int:
    """Запрашивает год рождения, повторяет при ошибке."""
    while True:
        user_input = input(f"В каком году родился {person_name}? ")
        if user_input.isdigit():
            return int(user_input)
        print("Пожалуйста, введите год числами!")

def ask_play_again() -> bool:
    """Спрашивает, хочет ли пользователь сыграть снова."""
    while True:
        answer = input("\nХотите начать игру сначала? (да/нет): ").lower().strip()
        if answer in ("да", "нет"):
            return should_play_again(answer)
        print("Пожалуйста, введите 'да' или 'нет'!")

def display_stats(stats: dict):
    """Печатает итоги."""
    print("\n====== ИТОГИ ВИКТОРИНЫ ======")
    print(f"Количество правильных ответов: {stats['correct']}")
    print(f"Количество ошибок: {stats['wrong']}")
    print(f"Процент правильных ответов: {stats['percent_correct']:.0f}%")
    print(f"Процент неправильных ответов: {stats['percent_wrong']:.0f}%")
    print("=============================")

# -------- 3. ОСНОВНАЯ ФУНКЦИЯ run (только связывает всё вместе) --------

def run():
    print("\n--- ДОБРО ПОЖАЛОВАТЬ В ВИКТОРИНУ 'ГОД РОЖДЕНИЯ' ---")
    while True:
        celebrities = get_celebrities()
        correct = 0
        wrong = 0

        for person in celebrities:
            user_year = ask_year(person["name"])
            if is_correct(user_year, person["year"]):
                print("Правильно!")
                correct += 1
            else:
                print(f"Неверно! (Правильный ответ: {person['year']})")
                wrong += 1

        stats = calculate_stats(correct, wrong, len(celebrities))
        display_stats(stats)

        if not ask_play_again():
            print("Спасибо за игру!")
            break
