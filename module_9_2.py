first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [e for e in first_strings if len(e) > 5]
second_result = [(e1, e2) for e1 in first_strings for e2 in second_strings if len(e1) == len(e2)]
third_result = {e: len(e) for e in first_strings + second_strings if len(e) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)