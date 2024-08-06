def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# 1. Функция с параметрами по умолчанию:
# print_params()
# print_params(a, b)
print_params(1, 'строка', True)  # вызов функции с разным количеством параметров
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров:
values_list = [18, 'Июнь', True]
values_dict = {'a': False, 'b': 'Кварц', 'c': 4.16}
print()
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:
print()
values_list_2 = ['Summer', 24]
print_params(*values_list_2, 42)
