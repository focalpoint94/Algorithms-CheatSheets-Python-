def generate_combinations(lists, prefix):
    if not lists:
        print(prefix)
        return
    first, rest = lists[0], lists[1:]
    for item in first:
        generate_combinations(rest, prefix + [item])

# 예제 리스트들
lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

generate_combinations(lists, [])
