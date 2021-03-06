import csv

from bs4 import BeautifulSoup

import config


def record_to_csv(data):
    with open(config.output_csv_file, 'a', encoding='cp1251', newline='') as file_w:
        writer = csv.writer(file_w, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)
    print('RECORD COMLETE!')


def extract_data_from_xml():
    with open(config.input_xml_file, 'r', encoding='utf=8') as file:
        xml_file = file.read()

    soup = BeautifulSoup(xml_file, 'lxml')
    data_from_yml = []
    for tag in soup.find_all('offer'):
        list1 = [
            tag['id'],
        tag.find('url').text,
        tag.find('name').text,
        tag.find('price').text,
        tag.find('picture').text,
        tag.find('description').text,
        ]
        data_from_yml.append(list1)
    return data_from_yml