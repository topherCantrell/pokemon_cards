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
    
    def __init__(self, fname):
        self._fname = fname
        with open(fname) as f:
            self._db = json.loads(f.read())
            
    def save(self):
        with open(self._fname,'w') as f:
            f.write(json.dumps(self._db,indent=2))

if __name__ == '__main__':
    db = CardDB('../sword_shield.json')
    db.save()    