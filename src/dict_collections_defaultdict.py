"""
used methods
collections.defaultdict
csv.DictReader()
"""

import csv
from collections import defaultdict
from datetime import datetime

start_time = datetime.now()
file_path = r'D:\ProgramFiles\GoogleDrive\PythonCode\github\ecevinoth\Python-DataStructure-and-Algorithm\data\developer_survey_2019\survey_results_public.csv'
with open(file_path, encoding='UTF8') as f:

    # read the file into dict class.
    csv_reader = csv.DictReader(f)

    # create dict class with default data type int. alternative to d={}; d.setdefault(k, [])
    counter = defaultdict(int)

    for line in csv_reader:
        counter[line['Hobbyist']] += 1

total = counter['Yes'] + counter['No']
yes_pct = (counter['Yes'] / total) * 100
no_pct = (counter['No'] / total) * 100

print(f' SOF survey : Hobbyist')
print(f'yes percent : {round(yes_pct, 2)}')
print(f' no percent : {round(no_pct, 2)}')
print(f'\nscript execution time : {datetime.now() - start_time}')
