def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        print("\n".join(data))
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


def search(book: list[str], info: str):
    """
    Находит в списке все записи по определенному критерию поиска
    Если нашлось несколько совпадений - запрашивает уточнение поиска и ищет вариант среди найденного списка.
    """
    finded_list = [person for person in book if info in person]
    if len(finded_list) == 1:
        return finded_list[0]
    elif len(finded_list) < 1:
        return 'Совпадений не найдено'       
    elif len(finded_list) > 1:
        print("\n".join(finded_list))
        clarify_data = input("Уточните данные по поиску: ")
        return search(finded_list, clarify_data)
    return 'Совпадений не найдено'
