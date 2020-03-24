import requests

def get_html_rows(s):
    ret = []
    while True:
        i = s.find('<tr>')
        if i<0:
            return ret
        j = s.find('</tr>',i)
        rd = s[i+4:j]
        if rd.startswith('<td'):
            ret.append(rd)
        s = s[j+5:]
        
def get_row_data(s):
    ret = []
    while True:
        i = s.find('<td')
        if i<0:
            return ret
        i = s.find('>',i)
        j = s.find('</td>',i)
        rd = s[i+1:j]
        ret.append(rd)
        s = s[j+5:]

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
    