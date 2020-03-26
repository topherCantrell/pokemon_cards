import json

class CardDB:
    
    '''
    DB Format:
    {
        "booster_boxes" : [ [1,2,3,4,...] ],  # List of pack-ids in the box
        "booster_singles" : [5,6,...], # List of single pack-ids
        "packs" : {
            "1" : ['1','2F','55','28F'] # Strings to include "FOIL/HOLO" designators or ENERGY type            
        },
        "decks" : {
            "803" : {
                "name" : "blahblah",
                "cards" : ['1','2',...]
            }
        },
        "cards" : {
            "1" : {
                # Lots of other stuff
            }
        }
    }    
    '''
    
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
            
    def get_card(self,id):
        if id[-1]=='H' or id[-1]=='F':
            id = id[0:-1]
        return self._db['cards'][id]
    
    def count_cards(self,cards):
        ret = {}
        for card in cards:
            if card in ret:
                ret[card] += 1
            else:
                ret[card] = 1
        return ret
            
    def get_all_cards(self):        
        
        owned_nums = []
        
        # From decks
        
        for deck_id in self.collection['decks']:
            owned_nums += self.cards['decks'][deck_id]['cards']
            
        for pack_id in self.collection['packs']:
            owned_nums += self.collection['packs'][pack_id]
        
        # TODO: Minus the ones in collection['gone']
        
        return owned_nums

if __name__ == '__main__':
    db = CardDB()
    db.save_cards()    
    db.save_collection()