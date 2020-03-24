import csv
import json

ENERGY_TYPES = ['METAL','WATER','ELECTRIC','FIRE','WATER','PSYCHIC','FIGHT','DARK','GRASS']
with open('../boosters.csv') as f:
    reader = csv.reader(f,delimiter=',')
    packs = {}
    for row in reader:
        if not row[-1]:
            continue
        if row[8] not in ENERGY_TYPES:
            raise Exception(f'Unknown energy type: {row[8]}')
        cards = []
        for c in row[1:]:
            cards.append(str(c))        
        packs[str(row[0])] = cards
        
    print(json.dumps(packs,indent=2))
         
     