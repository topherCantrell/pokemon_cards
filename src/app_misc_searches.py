import card_db

db = card_db.CardDB('../sword_shield.json')

def count_energies():
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
    
cards_owned = db.get_all_cards()

for match in db.ENERGY_TYPES+['NONE','']:
    total = 0
    for card in cards_owned:    
        if card in db.ENERGY_TYPES:
            continue
        if db.get_card(card)['color']==match:
            total = total + cards_owned[card]
            print(f'  {card} {cards_owned[card]}')
    
    print(f'{match} {total}')
    
print()

for match in db.ENERGY_TYPES:    
    print(f'{match} {cards_owned[match]}')
    
print()

total = 0
for card in cards_owned:
    total += cards_owned[card]
print(total)
    