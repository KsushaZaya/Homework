my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initial_value = 0

while initial_value < len(my_list):
    number = my_list[initial_value]
    initial_value = initial_value + 1
    if number == 0:
        continue
    elif number < 0:
        break
    elif number == len(my_list):
        print(number)
        print('Конец списка')
    else:
        print(number)
        