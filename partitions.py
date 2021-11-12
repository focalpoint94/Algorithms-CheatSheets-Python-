def partitions(s):
    if not s:
        yield []
    for i in range(1, len(s)+1):
        first, second = s[:i], s[i:]
        for p in partitions(second):
            yield [first] + p

for x in partitions('sexy'):
    print(x)
