import random


def get_random_password(n) -> str:
    s = 'abcdefghijklmnopqrstuvwxyz'
    str_lw = [i for i in s]
    str_up = [i for i in s.upper()]
    nums = [str(i) for i in range(10)]
    all_lists = str_up + str_lw + nums
    password_list = []
    for i in range(n):
        a = random.choice(all_lists)
        password_list.append(a)
    password = ''.join(password_list)

    return password


print(get_random_password(8))

