list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_num = max(list_numbers)
index_max_num = 0

for i in list_numbers:
    if i < max_num:
        index_max_num += 1
    else:
        break

list_numbers[index_max_num], list_numbers[-1] = list_numbers[-1], max_num
print(list_numbers)
