def run():
    while True:
        print("\n--- ДОБРО ПОЖАЛОВАТЬ В ВИКТОРИНУ 'ГОД РОЖДЕНИЯ' ---")

        celebrities = [
            {"name": "А.С. Пушкин", "year": 1799},
            {"name": "П.И. Чайковский", "year": 1840},
            {"name": "Юрий Гагарин", "year": 1934},
            {"name": "Альберт Эйнштейн", "year": 1879},
            {"name": "Леонардо да Винчи", "year": 1452},
        ]

        correct_answers = 0
        wrong_answers = 0
        total_questions = len(celebrities)

        for person in celebrities:
            while True:
                user_input = input(f"В каком году родился {person['name']}? ")
                if user_input.isdigit():
                    user_year = int(user_input)
                    break
                else:
                    print("Пожалуйста, введите год числами!")

            if user_year == person["year"]:
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неверно! (Правильный ответ: {person['year']})")
                wrong_answers += 1

        percent_correct = correct_answers * 100 / total_questions
        percent_wrong = wrong_answers * 100 / total_questions

        print("\n====== ИТОГИ ВИКТОРИНЫ ======")
        print(f"Количество правильных ответов: {correct_answers}")
        print(f"Количество ошибок: {wrong_answers}")
        print(f"Процент правильных ответов: {percent_correct}%")
        print(f"Процент неправильных ответов: {percent_wrong}%")
        print("=============================")

        while True:
            play_again = input("\nХотите начать игру сначала? (да/нет): ").lower().strip()
            if play_again in ("да", "нет"):
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'!")

        if play_again == "нет":
            print("Спасибо за игру!")
            break
