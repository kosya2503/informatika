import json  # импортируем нужный нам модуль


def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:  # считываем данные в json файле
        data = json.load(f)

    total = 0.0  # создаём переменную для искомой суммы
    for item in data:
        total += item['score'] * item['weight']  # пишем формулу произведения для элементов каждого словаря
    return round(total, 3)  # выводим результат


if __name__ == '__main__':  # функция выполнится при открытии файла main.py
    print(task())