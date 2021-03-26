import random

MAX_NB = 10
LIST_SIZE = 30
couples = []

# initial list

list_instance = [random.randint(0, MAX_NB) for _ in range(LIST_SIZE)]
ref_number = random.randint(0, MAX_NB)

# remove values higher than number

list_filtered = [elt for elt in list_instance if elt <= ref_number]


# remove duplicates values

list_processed = []

for elt in list_filtered:

    if elt not in list_processed:

        list_processed.append(elt)

    else:

        # particular case:
        # we check if the number is already in list_filtered & is present again (2 times) & is ref_number/2
        # otherwise we would miss it because we remove duplicate numbers

        if elt == ref_number / 2 and len(couples) == 0:

            couples.append((elt, elt))


# search couples

for i in range(int(len(list_processed) / 2)):

    for j in range(i + 1, len(list_processed)):

        if list_processed[i] + list_processed[j] == ref_number:

            couples.append((list_processed[i], list_processed[j]))


# print results

print(ref_number)
print(list_instance)
print(couples)
