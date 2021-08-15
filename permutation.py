from itertools import permutations, combinations, combinations_with_replacement

data = ['A', 'B', 'C', 'D']

# 순열 리스트
permut_list = list(permutations(data, 3))
print(permut_list)

# 조합 리스트
combin_list = list(combinations(data, 3))
print(combin_list)

# 조합 리스트 (중복 허용)
combin_list_with_replacement = list(combinations_with_replacement(data, 3))
print(combin_list_with_replacement)

# for문
for x in permutations(data, 2):
    print(list(x))
