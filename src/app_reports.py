import card_db

db = card_db.CardDB()

def get_energies(cards : list)->dict:
    '''Pick out all the energy cards from the given set of cards
    
    Args:
        cards (list): The list of card-ids to check
        
    Returns:
        dict : counts of each energy type
    '''        
    
    ret = {}
    for ct in cards:
        if ct in db.ENERGY_TYPES:
            if ct in ret:
                ret[ct]+=1
            else:
                ret[ct]=1
    return ret
        
def get_album_sleeves(cards):    
    '''Get the cards that belong in a sleeve in an album
    
    This combines all forms of cards of the same number.
    
    Args:
        cards (list): The list of card-ids to check
        
    Return:
        list : string representation for each card slot
    '''
    
    slots = []
    for _ in range(217): # 1..216 (0 isn't used)
        slots.append([])
    
    for ct in cards:
        # Energy cards don't go in an album
        if ct in db.ENERGY_TYPES:
            continue          
        if ct[-1]=='F':
            slots[int(ct[0:-1])].append('F')
        elif ct[-1]=='H':        
            slots[int(ct[0:-1])].append('H')
        else:
            slots[int(ct)].append('+')
        
    ret = ['']*217
    for i in range(1,216):
        contents = slots[i]
                
        # Sort the sleeve
        
        normals = 0
        foils = 0
        holos = 0
        
        for c in contents:
            if c=='H':
                holos +=1
            elif c=='F':
                foils += 1
            else:
                normals += 1
                
        ct = ''
        if foils:
            ct=ct + 'F'
            foils -=1
        if holos:
            ct=ct + 'H'
            holos -=1
        for _ in range(normals):
            ct = ct + '+'
        for _ in range(foils):
            ct = ct + 'F'
        for _ in range(holos):
            ct = ct + 'H'
            
        ret[i] = ct
    return ret

def added_packs(pack_ids=[]):

    cards = db.get_all_cards(not_packs=pack_ids)    
    alb_before = get_album_sleeves(cards)
    
    cards = db.get_all_cards()    
    alb_after = get_album_sleeves(cards)
    
    for i in range(1,204):
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
    total2 = 0
    cards = db.get_all_cards()    
    alb = get_album_sleeves(cards)
    for i in range(1,len(alb)):
        co = alb[i]
        total2 += len(co)
        if len(co)>4:
            total +=4
        else:
            total += len(co)
        while len(co)<4:
            co = co + '.'
        if co=='....':
            co = ''
        else:
            co = co[0:4]+'|'+co[4:]        
        ii = str(i)
        while len(ii)<3:
            ii = ' '+ii
        print(f'{ii} {co}')
    print(f'Total cards in albumn={total}. Total cards={total2}')
        
def show_discards():
    total = 0
    cards = db.get_all_cards()    
    alb = get_album(cards)
    for i in range(1,204):
        co = alb[i]
        total += len(co)
        j = len(co)
        if j<=4:
            continue
        co = co[4:]        
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
    
def show_needed(rarity):
    cards = db.get_all_cards()
    album = get_album_sleeves(cards)
    # TODO: albums should be lists ... not dictionaries
    
    for i in range(1,204):
        crd = db.cards['cards'][str(i)]
        if crd['rarity'] != rarity:
            continue
        co = album[i]
        if len(co)>=4:
            continue
        print(f'{i} {co}')    
        
    
show_needed('Common')    

#show_albumn()
        
#added_packs([86,87,88,89])

#show_albumn()

#show_discards()

#cards = db.get_all_cards()
#show_energies(cards)

#album = get_album(cards)
#print(len(cards))

#show_origins("20")
#show_origins("20F")

#show_origins("46")
#show_origins("46F")

#print(get_energies(cards))