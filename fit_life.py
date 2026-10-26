# Программа FitLife
print("-" * 40)
print("   Вас приветствует программа FitLife")
print("-" * 40)

# Шаг 1: Спрашиваем имя и возраст
user_name = input("Давайте познакомимся!\nКак вас зовут? ")
user_name = user_name.title()

user_age = input("Сколько вам полных лет? ")
user_age = int(user_age)  # Превращаем в число

# Шаг 2: Узнаём вес и рост
print("-" * 40)
print("Для расчета ИМТ и нормы воды в день:")
print("-" * 40)
user_weight = input("1. Укажите ваш вес в килограммах (например, 63.5): ")
user_weight = float(user_weight)  # Добавляем плавающую точку

user_height = input("2. Укажите ваш рост в метрах (например, 1.75): ")
user_height = float(user_height)  # Добавляем плавающую точку

# Шаг 3: Производим расчеты
bmi = user_weight / (user_height**2)
total_bmi = round(bmi, 2)

water_ml = user_weight * 30
water_l = water_ml / 1000

# Шаг 4: Выводим результат
print("=" * 30)
print("Ваш отчет FitLife готов! :)")
print("=" * 30)
print(f"Пользователь: {user_name} ({user_age} л.)")
print("Ваш Индекс Массы Тела:", total_bmi)
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("=" * 30)
print("Расчёт окончен. Будьте здоровы!")
