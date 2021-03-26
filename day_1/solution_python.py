import random
from itertools import combinations

MAX_NB = 10
LIST_SIZE = 30
couples = []

# initial list

list_instance = [random.randint(0, MAX_NB) for _ in range(LIST_SIZE)]
ref_number = random.randint(0, MAX_NB)

# getting couples with itertools (more practical approach)

list_couples = list(combinations(set(list_instance), 2))

# particular case: ref_number is an elt of the list *2

if ref_number / 2 in set(list_instance):
    elt = int(ref_number / 2)
    couples.append((elt, elt))

# computing couples

list_couples = [
    couple for couple in list_couples if (couple[0] + couple[1] == ref_number)
]

couples = couples + list_couples

# print results

print(ref_number)
print(list_instance)
print(couples)