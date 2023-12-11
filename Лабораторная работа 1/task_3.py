# TODO Найдите количество книг, которое можно разместить на дискете
sheets = 100
value = 1.44 * 1024*1024
strings = 50
chars = 25
amount = value / (4 * sheets * strings * chars)
print("Количество книг, помещающихся на дискету:", round(amount))

