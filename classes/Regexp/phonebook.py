# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
def process_phone(phone):
    if not phone:
        return ''
    ext_match = re.search(r'доб\.?\s*(\d+)', phone, re.I)
    ext = ext_match.group(1) if ext_match else None
    digits = re.sub(r'\D', '', phone)
    main_number = f"+7({digits[1:4]}){digits[4:7]}-{digits[7:9]}-{digits[9:11]}"

    if ext:
        return f"{main_number} доб.{ext}"

    return main_number


def process_fio(contact):
    fio = ' '.join(contact[:3]).split()
    fio.extend([''] * (3 - len(fio)))
    return fio[:3]


processed_contacts = []
for contact in contacts_list[1:]:
    lastname, firstname, surname = process_fio(contact)
    phone = process_phone((contact[5]))
    processed_contact = [
            lastname,
            firstname,
            surname,
            contact[3],
            contact[4],
            phone,
            contact[6]
    ]
    processed_contacts.append(processed_contact)

unique_contacts = {}
for contact in processed_contacts:
    key = (contact[0], contact[1])
    if key in unique_contacts:
        existing_contact = unique_contacts[key]
        for i in range(len(existing_contact)):
            if not existing_contact[i] and contact[i]:
                existing_contact[i] = contact[i]
    else:
        unique_contacts[key] = contact.copy()

result_list = [contacts_list[0]] + list(unique_contacts.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result_list)
pprint(result_list)
