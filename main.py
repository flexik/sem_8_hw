import functions as func


while True:
    print('1. Вывод 2. Добавление 3. Поиск 4. Изменение данных 5. Выход')
    mode = int(input("Введите номер режима работы со справочником: "))
    if mode == 1:
        func.show_data()
    elif mode == 2:
        func.add_data()
    elif mode == 3:
        func.find_data()
    elif mode == 4:
        func.change_data()
    else:
        break
