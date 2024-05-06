cars_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0

for (i, item) in enumerate(cars_list):
    print('Я езжу на автомабиле марки', item, '    | Шаг:', i, '    | Счетчик:', cars_count)
    cars_count += 10

