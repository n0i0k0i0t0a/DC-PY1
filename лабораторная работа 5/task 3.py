import random


def get_unique_list_numbers() -> list:
    k = []
    a = list(range(-10, 11))
    for i in range(15):
        z = random.choice(a)
        a = a[0:a.index(z)] + a[a.index(z)+1:]
        k.append(z)
    return k


list_unique_numbers = get_unique_list_numbers()

print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
print(len(list_unique_numbers))

