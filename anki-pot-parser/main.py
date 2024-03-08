import csv
import re
from stardict import DictCsv

source = '.\\pot.txt'
output = '.\\pot.csv'
ecdict = DictCsv(filename='ecdict.csv')
regex = r'\[(.*?)\]'

raw_data = []
with open(source) as f:
    for line in f:
        sections = line.split('\t')
        match = re.search(regex, sections[0])
        if match:
            word = match.group(1)
            val = ecdict.query(word)
            if val:
                definition = val.get('definition')
                translation = val.get('translation')
                raw_data.append([word, sections[1], definition, translation, sections[0]])
            else:
                print(word)

with open(output, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(raw_data)
