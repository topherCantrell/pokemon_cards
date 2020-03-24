import card_db

db = card_db.CardDB('../sword_shield.json')

energies = {}
for e in card_db.CardDB.ENERGY_TYPES:
    energies[e] = 0

card_counts = [0]*204
for pack_id in db._db['packs']:
    for card in db._db['packs'][pack_id]:        
        if card in card_db.CardDB.ENERGY_TYPES:
            energies[card]+=1
            continue
        if card[-1] == 'F' or card[-1] == 'H':
            card = card[0:-1]
        #print(card)
        card_counts[int(card)]+=1
            
print(energies)
print(card_counts)
    