# Задание №1 (частота встречаемости символа в строке)
def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    a = str_.split()
    alfabet_dict = {}
    for k in a:
        for i in k.lower():
            if i in alfabet_dict:
                if i.isalpha():
                    alfabet_dict[i] += 1
            else:
                if i.isalpha():
                    alfabet_dict[i] = 1
    return alfabet_dict


# Задание, где просят найти частоту слов


def freq_word(str_):
    listed = []
    word_dict = {}
    c = str_.lower().split('.')
    for i in c:
        if ',' in i and '!' in i:
            ind = i.find(',')
            ind_ = i.find('!')
            first = i[:ind]
            second = i[ind:ind_]
            listed.append(first)
            listed.append(second)
        elif ',' in i and '!' not in i:
            ind_1 = i.find(',')
            part_first = i[:ind_1]
            part_second = i[ind_1:]
            listed.append(part_first)
            listed.append(part_second)
        elif ',' not in i and '!' in i:
            ind_2 = i.find(',')
            part_2 = i[:ind_2]
            listed.append(part_2)
        else:
            listed.append(i)
        f_1 = listed[0].split()
        for i in listed[1:]:
            f_1 += i.split()
        f_1_1 = []
        for i in f_1:
            if i.isalpha():
                f_1_1.append(i)
        for i in f_1_1:
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1
    return word_dict


# Задание №2 (процентное отношение элемента по отношению ко всем символам)


def compare(dict_symbols):
    d = {}
    for i in dict_symbols.keys():
        d[i] = list(dict_symbols.values())[list(dict_symbols.keys()).index(i)] / sum(dict_symbols.values())
    return d


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(freq_word(main_str))
print(compare(get_count_char(main_str)))

