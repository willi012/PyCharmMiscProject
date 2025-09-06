import json

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data["agentId"])
print(data["paymentMethodData"][1])

age = 22
height = 1.72
name = "Vlad"
message = "ошибка формирования обратитесь к служебному специалисту"

while True:
    try:
        ticket = int(input("Введите 1 если есть билет, 0 если нет: "))

        if ticket == 1:
            print(age)
            print(height)
            print(name)
            break  # выходим из цикла
        elif ticket == 0:
            print(message)
            break  # тоже выходим
        else:
            print("Ошибка: допустимы только значения 0 или 1")
    except ValueError:
        print("Ошибка: нужно вводить число, а не текст")


addpayre = 1231

print(type(addpayre))

