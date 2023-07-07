def init(L,e,h):
    len = skipLen(L)

    #Erstelle die unterste Skipplist, sofern es noch keine gibt
    if len == 0 or L == None:
        end = Element(1,None,None)
        element = Element(e,None,end)
        start = Element(0,None,element)
        L = start
        len = 1
    
    #Sonst nehme die oberste skipliste
    else:
        end = suche(L,len)
        element = suche(L,e)
        start = L
        L = start

    #Erstelle die i-te Skippliste. Sie Zeigt auf die untere (vorigen Iteration erstellten) Skippliste
    for i in range(len+1,h+1):
            up_end = Element(i,end,None)
            up_element = Element(e,element,up_end)
            up_start = Element(0,start,up_element)
            
            #Merke für pointer für nächste Iteration (Auf diese wird von oben dann gezeigt)
            end = up_end
            element = up_element
            start = up_start
            L = start

    return L

def printList(L):
    start = L
    current = start
    while start != None:
        while current != None:
            print(current.name,end=' -> ')
            current = current.right
        start = start.down
        current = start
        print()
 
def skipLen(L):
    h = 0
    temp = L
    while temp != None:
        h +=1
        temp = temp.down
    return h

#fügt das element zu der liste hinzu und return das element
def add_one(temp,e,down):
    while e >= temp.right.name or temp.right == None:    #gehe die skippliste nach rechts und suche nach einen größeren element
        temp=temp.right

    new = Element(e,down,temp.right)                   #erstelle neues element
    temp.right = new                                   #pointer ausrichten

    return new

def einfügen(L,e,h):
    len = skipLen(L)    #länge der skippliste
    temp = L
        
    if len == 0 or L == None :
        return init(L,e,h)

    else:
        
        futur = h
        h = len

        while h<len:        #gehe die skippliste runter bis zur gewünschen höhe
            temp = temp.down
            len -=1
            
        newup = add_one(temp,e, None)       #füge das element zur in die richtige stelle ein für die derzeitige liste
        temp = temp.down                    #gehe eins nach unten
        h -= 1                              #^     

        while h != 0:                       #wiederhole das bis zur skipplisten höhe 1
            new = add_one(temp,e,None)
            temp = temp.down                   
            h -= 1                    

            #der vorherige eintrag muss auf den unteren eintrag zeigen
            newup.down = new
            newup = new

        if futur>len:
            return init(L,e,futur)

    return L

def suche(L,e):
    temp = L
    
    #gehe solange nach unten und das ende nicht erreicht wurde
    while temp != None:
        #gehe nach rechts solange e größer ist und das ende nicht erreicht wurde
        while e > temp.right.name and temp.right != None:
            temp = temp.right    #gehe nach rechts
        
        #teste ob e gefunden wurde
        if e == temp.right.name:
                return (temp.right, temp.right.name)
            
        #sonst speichere das nächstgrößte element und gehe nach unten
        nextbiggest = temp.right
        temp = temp.down        
    return (nextbiggest, nextbiggest.name)


class Element:
    def __init__(self, name, down, right):
        self.right = right
        self.down = down
        self.name = name

L = init(None,0.2,5)
L = einfügen(L,0.1,5)
L = einfügen(L,0.3,2)
L = einfügen(L,0.5,3)
L = einfügen(L,0.01,5)
L = einfügen(L,0.001,6)
printList(L)
#print(suche(L,0.24))