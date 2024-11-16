def all_variants(text):
    for e in range(len(text)):
        for j in range(e + 1, len(text) + 1):
            yield text[e:j]


a = all_variants("abcd")
for i in a:
    print(i)