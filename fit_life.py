# Программа FitLife

# Константы
SEPARATOR = "-" * 40
RESULT_SEPARATOR = "=" * 30
WATER_ML_PER_KG = 30
ML_IN_LITER = 1000


def main():
    """Запрашивает данные, считает ИМТ и норму воды, возвращает значения."""
    print(
        SEPARATOR,
        "   Вас приветствует программа FitLife",
        SEPARATOR,
        sep="\n",
    )

    # Шаг 1: Спрашиваем имя и возраст
    user_name = input("Давайте познакомимся!\nКак вас зовут? ").title()
    user_age = int(
        input(
            "Сколько вам полных лет? "
            "(введите кол-во полных лет, в целых числах) "
        )
    )

    # Шаг 2: Узнаём вес и рост
    print(
        SEPARATOR,
        "Для расчета ИМТ и нормы воды в день:",
        SEPARATOR,
        sep="\n",
    )
    user_weight = float(
        input("1. Укажите ваш вес в килограммах (например, 63.5): ").replace(
            ",", "."
        )
    )
    user_height = float(
        input("2. Укажите ваш рост в метрах (например, 1.75): ").replace(
            ",", "."
        )
    )

    # Шаг 3: Производим расчеты
    bmi = user_weight / (user_height**2)
    total_bmi = round(bmi, 2)
    water_ml = user_weight * WATER_ML_PER_KG
    water_l = water_ml / ML_IN_LITER

    return user_name, user_age, total_bmi, water_l


if __name__ == "__main__":
    user_name, user_age, total_bmi, water_l = main()

    print(
        f"{RESULT_SEPARATOR}\n"
        f"Ваш отчет FitLife готов! :)\n"
        f"{RESULT_SEPARATOR}\n"
        f"Пользователь: {user_name} ({user_age} л.)\n"
        f"Ваш Индекс Массы Тела: {total_bmi}\n"
        f"Рекомендуемая норма воды: {water_l} л. в день\n"
        f"{RESULT_SEPARATOR}\n"
        f"Расчёт окончен. Будьте здоровы!",
    )
