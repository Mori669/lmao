def find_pairs(n):
    final_pass = ''
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and i != j:
                final_pass += str(i) + str(j)
    return final_pass


while True:
    first_num = int(input('Число от 3 до 20: '))
    if 3 <= first_num <= 20:
        break
    else:
        print('Введите число от 3 до 20')

print(find_pairs(first_num))
