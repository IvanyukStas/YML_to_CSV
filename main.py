from bs4 import BeautifulSoup
import csv
import config
from finctions import extract_data_from_xml, record_to_csv

'''
КОВЕРТЕР ИЗ XML В CSV
'''



if __name__ == '__main__':
    data_from_yml = extract_data_from_xml()
    record_to_csv(data_from_yml)










