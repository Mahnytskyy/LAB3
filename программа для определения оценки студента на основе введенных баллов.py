score = int(input("Введите вашу оценку: "))

if score >= 90:
    print("Отлично! Ваша оценка А")
elif score >= 80:
    print("Здорово! Ваша оценка - B")
elif score >= 70:
    print("Хорошо! Ваша оценка - C")
elif score >= 60:
    print("Ваша оценка - D. Стоит повторить материал.")
else:
    print("Вы не сдали экзамен")
