def all_variants(text):
    for l in range(1, len(text) + 1):
        for st in range(len(text) - l + 1):
            yield text[st:st + l]


a = all_variants("abc")
for i in a:
    print(i)
