def custom_write(file_name, strings):
    string_position = {}
    file = open(file_name, 'w', encoding='utf-8')

    for line_number, string in enumerate(strings, start=1):
        byte_pos = file.tell()
        file.write(string + '\n')
        string_position[(line_number, byte_pos)] = string

    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
