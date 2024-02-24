from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате записать данные? \n\n"
    f"1 Вариант: \n"
    f"{name} \n {surname}\n {phone}\n {address}\n\n"
    f"2 Вариант: \n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберете вариант"))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число"))

    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name} \n {surname}\n {phone}\n {address}\n\n")

    elif var == 2:
        with open("data_second_variant.csv", "a", encoding="utf-8") as f:
            f.write( f"{name}; {surname}; {phone}; {address}\n")
    
    

def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
               data_first_list.append("".join(data_first[j:i+1])) 
               j = i
        
        print("".join(data_first_list))

    

    print("Вывожу данные из 2 файла: \n")
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)

def update_data():
    name_to_update = input("Введите имя для обновления: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
    updated = False
    with open("data_first_variant.csv", "w", encoding="utf-8") as f:
        for line in data_first:
            if name_to_update in line:
                new_name = input("Введите новое имя: ")
                new_surname = input("Введите новую фамилию: ")
                new_phone = input("Введите новый номер телефона: ")
                new_address = input("Введите новый адрес: ")
                f.write(f"{new_name} \n {new_surname}\n {new_phone}\n {new_address}\n\n")
                updated = True
            else:
                f.write(line)
    
    if not updated:
        print("Данные не найдены")

def delete_data():
    name_to_delete = input("Введите имя для удаления: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
    deleted = False
    with open("data_first_variant.csv", "w", encoding="utf-8") as f:
        for line in data_first:
            if name_to_delete not in line:
                f.write(line)
            else:
                deleted = True
    
    if not deleted:
        print("Данные не найдены")

