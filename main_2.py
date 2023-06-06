import os

from pprint import pprint

list_ = []

for filename in os.listdir(r"C:\Users\aasadaka\Desktop\Pythonius\print('study theory&tasks')\Netology_oop_hw_2_Sadaqa\Задание № 3"):
    with open(os.path.join(r"C:\Users\aasadaka\Desktop\Pythonius\print('study theory&tasks')\Netology_oop_hw_2_Sadaqa\Задание № 3", filename), 'r', encoding='utf8') as f:

        text = f.read()

        dict_ = {}

        strings_count = 0

        for line in text.split('\n'):
            strings_count += 1

        dict_[strings_count] = [text]
        dict_[strings_count].append(filename)
        list_.append(dict_)

# pprint(list_)
# print()

quantity_of_strings = []

for el in list_:
    for key, value in el.items():
        quantity_of_strings.append(key)

quantity_of_strings.sort()
# print(quantity_of_strings)

with open(r"C:\Users\aasadaka\Desktop\Pythonius\print('study theory&tasks')\Netology_oop_hw_2_Sadaqa\res_file", 'w', encoding='utf8') as res_file:

    for el in quantity_of_strings:
        for el_ in list_:
            for key, value in el_.items():
                if el == key:
                    res_file.write(value[1] + '\n')
                    res_file.write(str(el)+ '\n')
                    res_file.write(value[0]+'\n')

