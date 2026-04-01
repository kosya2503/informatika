# TODO Напишите функцию find_common_participants

def find_common_participants(c1,c2, r = ','):
    l1 = set(c1.split(r))
    l2 = set(c2.split(r))
    s = sorted(list(l1.intersection(l2)))
    # обе строки переводим вр мнржество, находим рбщее и сортируем
    return s

pf = "Иванов|Петров|Сидоров"
ps = "Петрорв|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(pf, ps, '|'))
