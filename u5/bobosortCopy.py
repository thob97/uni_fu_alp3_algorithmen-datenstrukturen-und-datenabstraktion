import random
import time
counter = 0

#erhöht die höhe einer skippliste oder erstellt sie, falls es keine gibt
def rise(L,h):
    len = skipLen(L)

    #Erstelle die unterste Skipplist, sofern es noch keine gibt
    if len == 0 or L == None:
        end = Element(1,None,None)
        start = Element(0,None,end)
        L = start
        len = 1
    
    #Sonst nehme die oberste skipliste
    else:
        end = suche(L,len)
        start = L
        L = start

    #Erstelle die i-te Skippliste. Sie Zeigt auf die untere (vorigen Iteration erstellten) Skippliste
    for i in range(len+1,h+1):
            up_end = Element(i,end,None)
            up_start = Element(0,start,up_end)
            
            #Merke für pointer für nächste Iteration (Auf diese wird von oben dann gezeigt)
            end = up_end
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

#fügt das element zu einer liste(von der skipplist) hinzu und return das element
def add_one(temp,e,down):
    global counter
    while e >= temp.right.name or temp.right == None:    #gehe die skippliste nach rechts und suche nach einen größeren element
        temp=temp.right
        counter +=1

    new = Element(e,down,temp.right)                   #erstelle neues element
    temp.right = new                                   #pointer ausrichten

    return new


def einfügen(L,e,h):

    #teste ob die höhe der skippliste erhöht werden muss    
    if h>skipLen(L):
        L = rise(L,h)

    len = skipLen(L)    #länge der skippliste
    temp = L            #zum iterieren


    while h<len:        #gehe die skippliste runter bis zur gewünschen höhe
        temp = temp.down
        len -=1
        
    newup = add_one(temp,e, None)       #füge das element in die richtige stelle ein für die derzeitige liste
    temp = temp.down                    #gehe eins nach unten
    h -= 1                              #^     
    while h != 0:                       #wiederhole das bis zur skipplisten höhe 1
        new = add_one(temp,e,None)
        temp = temp.down                   
        h -= 1                    

        #der vorherige eintrag muss auf den unteren eintrag zeigen
        newup.down = new
        newup = new
        
    return L

#suche gibt das gesucht element zurück, sowie das element, was auf das gesuchte element zeigt
def suche(L,e):
    global counter
    temp = L
    
    #gehe solange nach unten solang das ende nicht erreicht wurde
    while temp != None:
        #gehe nach rechts solange e größer ist und das ende nicht erreicht wurde
        while e > temp.right.name and temp.right != None:
            #gehe nach rechts
            temp = temp.right    
            counter +=1
        
        counter +=1
        #teste ob e gefunden wurde
        if e == temp.right.name:
                return (temp, temp.name, temp.right, temp.right.name)
            
        #sonst speichere das nächstgrößte element und gehe nach unten
        next = temp
        nextbiggest = temp.right
        temp = temp.down        
    return (next, next.name, nextbiggest, nextbiggest.name)

def lösche(L,e):
    elements = suche(L,e)

    #falls e gefunden wurde, lösche alle e's in der liste
    if e == elements[3]:
        #solange nicht am ende der liste angekommen ist
        while True :
            #update die pointer
            elements[0].right = elements[0].right.right
            #'lösche' das element
            elements[2].name = None
            elements[2].down = None
            elements[2].right = None
            
            #falls am ende der liste angekommen abbruch der whileschleife
            if elements[0].down == None:
                break
            #gehe eins weiter nach unten und suche das element erneut
            elements = suche(elements[0].down,e)
    return L
     

class Element:
    def __init__(self, name, down, right):
        self.right = right
        self.down = down
        self.name = name

L = rise(None,5)
L = einfügen(L,0.1,5)
L = einfügen(L,0.3,2)
L = einfügen(L,0.5,3)
L = einfügen(L,0.01,5)
L = einfügen(L,0.2,6)
L = lösche(L,0.2)
printList(L)
#print(suche(L,0.24))

#######################        tests       #######################

def randomhight(p):
    h = 1
    coin = random.random()
    while coin < p:
        h +=1
        coin = random.random()
    return h

counter = 0
L = None

wahrscheinlichkeiten = [0.6,0.5,0.3,0.1,0.05]
durchläufe = 10

#mit wahrscheinlichkeit für die höhe p
for p in wahrscheinlichkeiten:
    
    begin = time.time()
    counter = 0
    #10 Durchläufe
    for k in range (durchläufe):
        #Erzeuge 20.000.000 Keys
        L = None
        for i in range(1,2000+1):
            zahl = random.random()
            höhe = randomhight(p)
            L = einfügen(L,zahl,höhe)
        
            #Nach 1000 Erzeugten keys Suche 2000 Keys
            if i%1000 == 0:
                for j in range(1,2000+1):
                    e = suche(L,random.random())
                    #500 dieser gesuchten Keys sollen gelöscht werden. (Also jeder 4te)
                    if j%4 == 0:
                        lösche(L,e[3])
    
    end = time.time()
    print('Wahrscheinlichkeit:',p, ', Average_Counter: ' , counter/10 , ', Average_Exec_Time: ' , end-begin/10)

