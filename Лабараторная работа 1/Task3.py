stranitsi = 100
stroki = 50
symvoli = 25
byte_v_symvole = 4

# Объем дискеты в байтах (исправляем запятую на точку)
volume = 1.44 * 1024 * 1024  # ~1 509 949 байт

# Объем одной книги в байтах
v_knige = stranitsi * stroki * symvoli * byte_v_symvole  # 500 000 байт

# Количество книг (целочисленное деление)
kolichestvo_knig = volume // v_knige

print("Количество книг, помещающихся на дискету:", int(kolichestvo_knig))