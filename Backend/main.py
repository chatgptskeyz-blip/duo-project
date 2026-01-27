print("=== КАЛЬКУЛЯТОР ИМТ ===")

weight = float(input("Вес (кг): "))
height = float(input("Рост (м): "))

bmi = weight / (height ** 2)

print(f"\nТвой ИМТ: {bmi:.2f}")

if bmi < 18.5:
    print("Недостаточный вес")
elif 18.5 <= bmi < 25:
    print("Нормальный вес")
elif 25 <= bmi < 30:
    print("Избыточный вес")
else:
    print("Ожирение худей сука")
