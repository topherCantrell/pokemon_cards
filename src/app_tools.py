from card_db import CardDB

db = CardDB('../sword_shield.json')

box = db._db['booster_boxes'][0]

for pack_id in box:
    pack = db._db['packs'][str(pack_id)]
    for card_id in pack:
        org_id = card_id
        if card_id in CardDB.ENERGY_TYPES:
            print(card_id)
            continue
        if card_id[-1]=='H' or card_id[-1]=='F':
            card_id = card_id[0:-1]
        card = db._db['cards'][str(card_id)]
        print(f'{org_id} {card["name"]}')

#print(box)