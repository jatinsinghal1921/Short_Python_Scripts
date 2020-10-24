import itertools
import operator



alpha_data = ['a', 'b', 'c', 'd']

result = itertools.permutations(alpha_data, r = 2)
for each in result:
    print(each)

