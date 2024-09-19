def print_params(a=1, b='строка', c = True):
    return a, b, c


print(print_params)

print(2, 'текст', False)
print(print_params(a=3, c=True))
print(print_params())
print(print_params(b='новая строка'))
print(print_params(b=25, c = [1,2,3]))

values_list = [3.14, 'PI', False]
values_dict = {'a': 99, 'b': 'словарь', 'c': [4, 5, 6]}

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

