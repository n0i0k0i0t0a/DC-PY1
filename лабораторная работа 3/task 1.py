src = not False and True or False and not True

# result = True and True or False and False - избавились от "not" (отрицание)
# result = True or False - избавились от "and" (логический оператор "И")
result = True
# избавились от "or" (логический оператор "ИЛИ")
print(src == result)

