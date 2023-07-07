import random
import time
from time import sleep
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
#(suche() funktioniert hier nicht, da es viel mehr vergleiche brauchen würde)
def add_one(temp,e):
    global counter
    while e >= temp.right.name and temp.right != None:    #gehe die skippliste nach rechts und suche nach einen größeren element
        temp=temp.right
        counter +=1

    new = Element(e,None,temp.right)                   #erstelle neues element
    temp.right = new                                   #pointer ausrichten

    return (temp,new)



def einfügen(L,e,h):

    #teste ob die höhe der skippliste erhöht werden muss    
    if h>skipLen(L):
        L = rise(L,h)

    len = skipLen(L)    #länge der skippliste
    temp = L            #zum iterieren


    while h<len:        #gehe die skippliste runter bis zur gewünschen höhe
        temp = temp.down
        len -=1
        

    tupl = add_one(temp,e)              #füge das element in die richtige stelle ein für die derzeitige liste, und gebe das element, was auf das eingefügte element zeigt zurück
    temp = tupl[0]                      #temp -> newup
    newup = tupl[1]                     
    temp = temp.down                    #gehe eins nach unten
    h -= 1                              #^     
    while h != 0:                       #wiederhole das bis zur skipplisten höhe 1
        tupl = add_one(temp,e)
        temp = tupl[0]
        new = tupl[1]

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
        while temp.right != None and e > temp.right.name:
            #gehe nach rechts
            temp = temp.right    
            counter +=1
        
        counter +=1
        #teste ob e gefunden wurde
        if temp.right != None and e == temp.right.name:
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
            #gehe eins weiter nach unten und suche das element erneut (.down spart ein paar vergleiche)
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
L = einfügen(L,0.999,20)
L = lösche(L,0.999)
suche(L,0.9)
einfügen(L,0.9,16)
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

wahrscheinlichkeiten = [0.7,0.6,0.5,0.3,0.1,0.05]
durchläufe = 10

#mit wahrscheinlichkeit für die höhe p
for p in wahrscheinlichkeiten:
    
    begin = time.time()
    counter = 0
    #10 Durchläufe
    for k in range (durchläufe):
        #Erzeuge 20.000.000 Keys
        L = None
        for i in range(1,20000+1):
            zahl = random.random()
            höhe = randomhight(p)
            L = einfügen(L,zahl,höhe)
        
            #Nach 1000 Erzeugten keys Suche 2000 Keys
            if i%1000 == 0:
                for j in range(1,2000+1):
                    randomfloat = random.random()
                    e = suche(L,randomfloat)
                    #500 dieser gesuchten Keys sollen gelöscht werden. (Also jeder 4te)
                    if j%4 == 0:
                        #lösche nur die Zahl, falls sie auch in der liste existiert
                        if e[3] == randomfloat:
                            lösche(L,e[3])
    
    end = time.time()
    print('Wahrscheinlichkeit:',p, ', Average_Counter: ' , counter/10 , ', Average_Exec_Time: ' , (end-begin)/10)

