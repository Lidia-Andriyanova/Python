# Составить словарь слов из файда jack.txt
from pprint import pprint

with open('jack.txt', 'r', encoding='utf-8') as file_info:
    jack_str = file_info.read()

jack_list = jack_str.lower().replace('\ufeff', '').split()

jack_list = list(filter(lambda elem: elem not in [',', '.'], jack_list))

word_dict = {}
for elem in jack_list:
    word_dict[elem] = word_dict.get(elem, 0) + 1

print('Словарь слов:')
pprint(word_dict)
