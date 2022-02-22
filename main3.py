try:
    age = input("Введите ваш возраст:")
    age_int = int(age)
    if (age_int <= 18) :
        print("Ха-ха")
    if (19 <= age_int <= 30):
        print("Ой")
    if (31 <= age_int <= 50):
        print(":)")
    if ( age_int >= 50):
        print("Шутка")
    print("Ваш возраст", age_int)
except ValueError:
    print("Введите, пожалуйста, число :(")
