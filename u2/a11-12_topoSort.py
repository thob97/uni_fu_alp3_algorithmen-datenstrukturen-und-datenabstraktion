import intReader

def TopoSort():
    print ("Topologischen Sortieren.")
    # Einlesen
    input = intReader.readInt()
    n = next(input)

    # Inititalisieren array:
    Knotenliste = [None] + [ Knoten(i) for i in range(1,n+1) ]

    
    # Einlesen Kanten
    try:
        while True:
            e = Knotenliste[next(input)]
            f = Knotenliste[next(input)]
            x = Kante(e,f)
            x.next = e.ersterNachfolger
            e.ersterNachfolger = x
            x.next2 = f.letzterVorgaenger              ##### Iterator für die Vorgaenger #####
            f.letzterVorgaenger = x                    ##### zeigt auf den letzten Vorgaenger #####
            f.anzVorgänger += 1
            e.anzNachvolger += 1                       ##### speichert die Anzahl der Nachvolger #####
    except StopIteration:
        pass
        
    # Vorbereiten:
    freieKnoten = [None]*n
    # explizit programmierter Stapel;
    # könnte auch mit append() (=push) und pop() geschrieben werden.    
    AnzfreieKnoten = 0;
    for i in range(1,n+1):
        e = Knotenliste[i]
        if e.anzVorgänger==0:
            freieKnoten[AnzfreieKnoten]=e
            AnzfreieKnoten += 1

    for i in freieKnoten:                            ##### removes freieKnoten from Knotenliste ##### 
        if i != None:
            Knotenliste.remove(i)

    # Sortieren:
    print()
    for i in range(1,n+1):
        if AnzfreieKnoten == 0:
            return find_kreis(Knotenliste, freieKnoten, n)
        # Wähle einen Knoten ohne Vorgänger
        AnzfreieKnoten -= 1
        x = freieKnoten[AnzfreieKnoten]
        #print(x)
        # Entferne ausgehende Kanten:
        z = x.ersterNachfolger
        while z != None:
            z.v.anzVorgänger -= 1
            if z.v.anzVorgänger == 0:
                freieKnoten[AnzfreieKnoten]=z.v
                Knotenliste.remove(z.v)                 ##### removes freieKnoten from Knotenliste #####
                AnzfreieKnoten += 1
            z = z.next


#############################  New  #########################################

def find_kreis(Knotenliste, freieKnoten, n):
    #Vorbereiten -> Makiere welche Knoten keine Nachvolger haben
    n = len(Knotenliste) - 1
    freieKnoten = [None]*n
    AnzfreieKnoten = 0
    for i in range(1,n+1):
        e = Knotenliste[i]
        if e.anzNachvolger==0:
            freieKnoten[AnzfreieKnoten]=e
            AnzfreieKnoten += 1

    #removes freieKnoten from Knotenliste
    for i in freieKnoten:   
        if i != None:
            #print(i)
            Knotenliste.remove(i) 

    #
    for i in range(1,n+1):

        #if AnzahlFreieKnoten == 0 -> only Kreis remains in Knotenliste
        if AnzfreieKnoten == 0:
            print("Ein oder mehrere Kreise in:")
            for i in Knotenliste:
                if i != None:
                    print(i)
            return

        # Wähle einen Knoten ohne Nachvolger
        AnzfreieKnoten -= 1
        x = freieKnoten[AnzfreieKnoten]
        # Entferne eingehende Kanten & Knoten aus Knotenliste:
        z = x.letzterVorgaenger
        while z != None:
            z.u.anzNachvolger -= 1
            if z.u.anzNachvolger == 0:
                freieKnoten[AnzfreieKnoten]=z.u
                Knotenliste.remove(z.u)    
                AnzfreieKnoten += 1
            z = z.next2
            
#test eingabe
# 8
# 1 2 1 3 2 3 4 1 4 5 4 7 5 6 6 1 7 8 8 4
# -> kreis in 4 - 7 - 8
#############################  till here  #########################################

class Knoten:
    def __init__(self, i):
        self.Name = i
        self.anzVorgänger = 0
        self.anzNachvolger = 0              ##### changed here ####
        self.ersterNachfolger = None        
        self.letzterVorgaenger = None       ##### changed here ####
    def __str__(self):
        return str(self.Name)

class Kante:
    def __init__(self, u, v):
        self.u = u
        self.v = v

TopoSort()        
