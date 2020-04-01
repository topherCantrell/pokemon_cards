import json

class CardDB:
           
    ENERGY_TYPES = ['METAL','WATER','ELECTRIC','FIRE','WATER','PSYCHIC','FIGHT','DARK','GRASS']
    
    SET_FILENAME = '../sword_shield.json'
    COLLECTION_FILENAME = '../my_collection.json'
    
    def __init__(self):        
        with open(CardDB.COLLECTION_FILENAME) as f:
            self.collection = json.loads(f.read())
        with open(CardDB.SET_FILENAME) as f:
            self.cards = json.loads(f.read())
            
    def save_collection(self):
        with open(CardDB.COLLECTION_FILENAME,'w') as f:
            f.write(json.dumps(self.collection,indent=2))
            
    def save_cards(self):
        with open(CardDB.SET_FILENAME,'w') as f:
            f.write(json.dumps(self.cards,indent=2))
            
    #
            
    def get_card_info(self,id):
        if id[-1]=='H' or id[-1]=='F':
            id = id[0:-1]
        return self.cards[id]
    
    def get_number_from_id(self,id):
        if id[-1]=='H' or id[-1]=='F':
            id = id[0:-1]
        return int(id)
    
    def count_cards(self,card_ids):
        ret = {}
        for card in card_ids:
            if card in ret:
                ret[card] += 1
            else:
                ret[card] = 1
        return ret
            
    def get_all_owned_cards(self,not_packs=[],not_decks=[],skip_gone=True):        
        
        owned_ids = []
        
        # From decks
        
        for deck_id in self.collection['decks']:
            if deck_id in not_decks or int(deck_id) in not_decks:
                continue
            owned_ids += self.cards['decks'][deck_id]['cards']
            
        for pack_id in self.collection['packs']:
            if pack_id in not_packs or int(pack_id) in not_packs:
                continue
            owned_ids += self.collection['packs'][pack_id]
        
        # TODO: Minus the ones in collection['gone']
        
        return owned_ids

if __name__ == '__main__':
    db = CardDB()
    db.save_cards()    
    db.save_collection()