import re
existingSlots=int(notepad.prompt('How many cards are before these in the cart?', 'Cart size?','0'))
delta=None
minSlot=None
def countSlots(contents, lineNumber, totalLines):
    global minSlot
    global delta
    match=re.search(r"<slots>(\d+)</slots>",contents)
    if(match):
        num=int(match.group(1))
        print str(num)
        if(minSlot == None or num < minSlot):
            minSlot=num
            delta=existingSlots-num
            print "min slot %s, delta %s" %(str(minSlot),str(delta))
        # if(delta == None):
        # newcontents = re.sub(r"<slots>(\d+)</slots>","<slots>%s</slots>" % str(num + delta),contents)
        # print newcontents
        # editor.replaceWholeLine(lineNumber, newcontents)
        # cardCount+=1

editor.forEachLine(countSlots)
totalCards=0
def calculate(match):
    global totalCards
    newVal=int(match.group(1)) + delta;
    print('newVal %s, totalCards %s' %(str(newVal), str(totalCards)))
    if(newVal > totalCards):
        totalCards=newVal
    return '<slots>%s</slots>' % (str(newVal))
    
editor.rereplace('<slots>(\d+)</slots>', calculate)
totalCards=int(notepad.prompt('How many total cards?', 'Total Cart Size?', str(totalCards)))
editor.rereplace('<quantity>(\d+)</quantity>', '<quantity>%s</quantity>' % (str(totalCards)))
items=[18,36,55,72,90,108,126,144,162,180,198,216,234,396,504,612]

cardBracket=-1
for index, item in enumerate(items):
    if(totalCards < item):
        cardBracket = item
        break;
cardBracket=int(notepad.prompt('You have %s cards, set total cards to %s?' %(totalCards,cardBracket), 'Total Cards?', str(cardBracket)))
editor.rereplace('<bracket>\d+</bracket>', '<bracket>%s</bracket>' % (str(cardBracket)))

def cardback(match):
    remove = notepad.prompt('You have a global card-back, remove it? ["OK" to remove, "Cancel" to keep]', 'Remove global cardback?','')
    if( remove != None ):
       return ''
    return match.group(0)

editor.rereplace('<cardback>[^<]*</cardback>', cardback)
