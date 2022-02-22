name = input("Ваше имя: ")
print("Длина вашего имени", len(name) , "символа")
age = int(input("Ваш возраст: "))
sum = 0
while (age != 0):
    sum = sum + age % 10
    age = age // 10
age_1 = int(input("Повторите возраст: "))
proz = 1
while (age_1 != 0):
    proz = proz * (age_1 % 10)
    age_1 = age_1 // 10
print("Cумма вашего возраста", sum, '\n', "Произведение вашего возраста", proz)
