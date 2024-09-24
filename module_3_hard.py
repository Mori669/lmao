def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (int, float)):
        return data

    elif isinstance(data, str):
        return len(data)

    elif isinstance(data, dict):
        for k, v in data.items():
            total_sum += calculate_structure_sum(k)
            total_sum += calculate_structure_sum(v)

    elif isinstance(data, (list, tuple, set)):
        for i in data:
            total_sum += calculate_structure_sum(i)

    return total_sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)