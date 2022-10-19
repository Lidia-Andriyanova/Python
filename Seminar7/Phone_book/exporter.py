import json
import csv

def export_json(file_name, phone_dict):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(phone_dict, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))
        # json.dump(phone_dict, f)


def export_csv(file_name, phone_dict):
    phone_lst = []
    for k, v in phone_dict.items():
        row_dict = dict()
        row_dict['phone'] = k
        row_dict['last_name'] = v[0]
        row_dict['first_name'] = v[1]
        phone_lst.append(row_dict)
    with open(file_name, 'w', encoding='utf-8') as f:
        fieldnames = ['phone', 'last_name', 'first_name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(phone_lst)


