import requests
import json

def get_html_rows(s,keep_headers=False):
    ret = []
    while True:
        i = s.find('<tr>')
        if i<0:
            return ret
        j = s.find('</tr>',i)
        rd = s[i+4:j]        
        if keep_headers:
            ret.append(rd)
        else:
            if rd.startswith('<td'):
                ret.append(rd)
        s = s[j+5:]
        
def get_row_data(s):
    ret = []
    while True:
        i = s.find('<t')        
        if i<0:
            return ret
        i = s.find('>',i)
        j = s.find('</t',i)        
        rd = s[i+1:j]
        ret.append(rd)
        s = s[j+5:]
        
def get_card_list():
    
    color_trans = {
        'Lightning' : 'ELECTRIC',
        'Psychic' : 'PSYCHIC',
        'Darkness' : 'DARK',
        'Metal' : 'METAL',
        'Fighting' : 'FIGHT',
        'Colorless' : 'NONE',
        '' : '',
        'Fire' : 'FIRE',
        'Grass' : 'GRASS',
        'Water' : 'WATER'       
        }
    
    g = requests.get('https://bulbapedia.bulbagarden.net/wiki/Sword_%26_Shield_(TCG)')
    
    s = g.text
    
    i = s.index('Set list')
    for _ in range(7):
        i = s.index('<table',i+1)
    
    j = s.index('</table>',i)
    
        
    s = s[i:j].replace('\n','')
        
    rows = get_html_rows(s)
    
    cards = {}
        
    for row in rows:
        data = get_row_data(row)
        cn = data[0].strip()
        cn = cn.split('/')
        cn = int(cn[0])
                     
        name = data[2]
        i = name.index('>')
        j = name.index('<',i)
        name = name[i+1:j]
        
        color = data[3]
        i = color.find('alt="')
        if i>=0:
            j = color.find('"',i+5)
            color = color[i+5:j]
        else:
            color = ''
        color = color_trans[color]
        
        rare = data[4]
        i = rare.index('title="')+7
        j = rare.index('"',i)
        rare = rare[i:j]
    
        card = {'id':cn, 'name':name, 'color':color, 'rarity':rare}
        cards[str(cn)] = card
        
    print(json.dumps(cards,indent=2))
    

def get_deck_data():
    
    g = requests.get('https://bulbapedia.bulbagarden.net/wiki/Rillaboom_Theme_Deck_(TCG)')
    
    s = g.text
    
    i = s.index('Deck list')
    j = s.index('</table>',i)
    
    s = s[i:j].replace('\n','')
    
    rows = get_html_rows(s)
    for row in rows:
        data = get_row_data(row)
        mult = int(data[0][0:-1].strip())
        i = data[1].find('title="')+7
        j = data[1].find('"',i)
        title = data[1][i:j]
        i = title.find('; Shield ')
        if i<0:
            title = title.split(' ')[0].upper()
        else:
            title = title[i+9:-1]
        if data[2].find('Rare Holo')>=0:
            holo = 'H'
        else:
            holo = ''
        for m in range(mult):
            print(f'"{title}{holo}",',end='')
        print()

get_card_list()    