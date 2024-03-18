import re
from stardict import DictCsv
import csv

source = '.\\pot.txt'
output = '.\\result.csv'
err = '.\\error.txt'
ecdict = DictCsv(filename='ecdict.csv')
regex = r'\[(.*?)\]'

raw_data = []
with open(source, 'r') as f, open(output, 'w') as d, open(err, 'w') as e:
    writer = csv.writer(d)
    for line in f:
        sections = line.split('\t')
        match = re.search(regex, sections[0])
        # if block bracket exist
        if match:
            word = match.group(1)
            example = sections[0] or ''
            cn_example = sections[1] or ''
        else:
            word = sections[0]
            example = ''
            cn_example = ''
        val = ecdict.query(word)
        if val:
            definition = val.get('definition')
            translation = val.get('translation')
            writer.writerow([word, definition, translation, example, cn_example])
        else:
            e.write(f'{line}')
