def pass_by_code(code):
    pass_code = 0
    for i in range(1, code):
        for j in range(i+1, code):
             if code % (i+j)  == 0:
                pass_code = add_digit_right(pass_code,i, j)

    return pass_code

def rand_stone():
    import random
    stone = random.randint(3, 20)
    print(stone)
    return stone

def add_digit_right(sum_number, add_number1, add_number2):
    sum_string = str(sum_number) + str(add_number1) + str(add_number2)
    return int(sum_string)

print(pass_by_code(rand_stone()))
