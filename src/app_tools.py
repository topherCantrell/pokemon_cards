from card_db import CardDB


def show_discards():
    db = CardDB()
    
    cards = db.get_all_cards()
    
    slots = []
    for _ in range(250):
        slots.append([])
    
    for ct in cards:
        if ct in db.ENERGY_TYPES:
            continue          
        if ct[-1]=='F' or ct[-1]=='H':        
            slots[int(ct[0:-1])].append('*')
        else:
            slots[int(ct)].append('.')
        
    total_discard = 0
    for i in range(1,250):
        contents = slots[i]
        if len(contents)<=4:
            continue
        
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
           
        #print(f'{i} {ct}')
        print(f'{i} {ct[4:]}')
        total_discard += len(ct[4:])
    
    print(total_discard)
    
show_discards()