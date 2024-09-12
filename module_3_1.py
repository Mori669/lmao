def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    ret = [len(string), string.upper(), string.lower()]
    return tuple(ret)


def is_contains(string, u_list):
    count_calls()
    fl = False
    for e in u_list:
        if string.upper() in e.upper():
            fl = True
            break
    return fl


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
