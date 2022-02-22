name = input("Введите ваше имя: ")
name_1 = name.strip()
print("Ваше имя", name_1)
try:
    age = input("Введите ваш возраст: ")
    age_int = int(age)
    if (0 <= age_int <= 150) :
        print("Ваш возраст", age_int)
    else:
        print("Неправда!")
except ValueError:
    print("Введите, пожалуйста, число :(")