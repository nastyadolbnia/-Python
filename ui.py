from logger import input_data, print_data, update_data, delete_data

def interface():
    print("Добрый день! Вы попали в бот-справочник \n 1 Записать данные \n 2 Вывод данных")
    command = int(input("Введите число"))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Неправильный ввод")
        command = int(input("Введите число "))

    if command == 1:
        input_data()
    elif command == 1:
        print_data()
    elif command == 3:
        update_data
    elif command == 4:
        delete_data

    



