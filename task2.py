def get_count_char(main_str):
    letter_ = main_str.lower()
    letter_ = letter_.replace(".","")
    letter_ = letter_.replace(",","")
    letter_ = letter_.replace("!","")
    letter_ = "".join(letter_.split())
    letter_.isalpha()
    letter_list = list(letter_)
    letter_dict = {}
    default_count = 0
    for letter in letter_list:
        letter_dict[letter] = letter_dict.get(letter, default_count) + 1
    return letter_dict
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
get_count_char(main_str)
print(get_count_char(main_str))

def second_f(dict_):
    dict2 = {}
    for letter, value in dict_.items():
        total_value = sum(dict_.values())
        num_ = round(value / total_value, 2)
        dict2[letter] = dict2.get(letter, num_)
    return dict2
print(second_f(dict_))



