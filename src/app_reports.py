import card_db

db = card_db.CardDB()

def get_energies(cards):
    ret = {}
    for ct in cards:
        if ct in db.ENERGY_TYPES:
            if ct in ret:
                ret[ct]+=1
            else:
                ret[ct]=1
    return ret
        
def get_sleeves(cards):    
    
    slots = []
    for _ in range(204):
        slots.append([])
    
    for ct in cards:
        if ct in db.ENERGY_TYPES:
            continue          
        if ct[-1]=='F' or ct[-1]=='H':        
            slots[int(ct[0:-1])].append('*')
        else:
            slots[int(ct)].append('.')
        
    total_discard = 0
    ret = {}
    for i in range(1,204):
        contents = slots[i]
                
        # Sort the sleeve
        
        normals = 0
        foils = 0
        
        for c in contents:
            if c=='*':
                foils += 1
            else:
                normals += 1
                
        ct = ''
        if foils:
            ct='*'
            foils -=1
        for _ in range(normals):
            ct = ct + '.'
        for _ in range(foils):
            ct = ct + '*'
            
        ret[i] = ct
    return ret

def added_packs(pack_ids=[]):

    cards = db.get_all_cards(not_packs=pack_ids)    
    alb_before = get_album(cards)
    
    cards = db.get_all_cards()    
    alb_after = get_album(cards)
    
    for i in range(1,250):
        ca = alb_after[i]
        cb = alb_before[i]
        
        if ca and not cb:
            print(f'NEW: {i} {alb_after[i]}')
            continue        
            
        if ca == cb:
            continue
        
        if len(cb)>=4 and cb[0:4] == ca[0:4]:
            print(f'NOTHING TO DO: {i} {cb} -> {ca}')
            continue
        
        print(f'{i} {cb} -> {ca}')
               
def show_albumn():
    total = 0
    cards = db.get_all_cards()    
    alb = get_album(cards)
    for i in range(1,204):
        co = alb[i]
        if len(co)>4:
            co = co[0:4]
        total += len(co)
        print(f'{i} {co}')
    print(f'Total cards: {total}')
        
def show_discards():
    total = 0
    cards = db.get_all_cards()    
    alb = get_album(cards)
    for i in range(1,204):
        co = alb[i]
        j = len(co)
        if j<=4:
            continue
        co = co[4:]
        total += len(co)
        print(f'{i} {co}')
    print(f'Total cards: {total}')
    
def show_energies(cards):
    energies = get_energies(cards)
    total = 0
    for en in energies:
        print(f'{en} {energies[en]}')
        total += energies[en]
    print(f'Total cards: {total}')
    
def show_sleeves(cards):
    get_sleeves(cards)
    
def show_origins(card_id):
    
    total = 0
    # Find all decks
    for deck_id in db.cards['decks']:
        for cd in db.cards['decks'][deck_id]['cards']:
            if cd==card_id:
                print(f'Card {cd} in deck {deck_id}')
                total+=1
                
    # Find all packs
    for pack_id in db.collection['packs']:
        for cd in db.collection['packs'][pack_id]:
            if cd==card_id:
                print(f'Card {cd} in pack {pack_id}')
                total+=1
    
    print(f'Total {card_id} cards: {total}')
    
    
    
    
        
#added_packs([41,42,43,44,45])

#show_albumn()

#show_discards()

cards = db.get_all_cards()
show_energies(cards)

#album = get_album(cards)
print(len(cards))

show_origins("20")
show_origins("20F")

show_origins("46")
show_origins("46F")

#print(get_energies(cards))