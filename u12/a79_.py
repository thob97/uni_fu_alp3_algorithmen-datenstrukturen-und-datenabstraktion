#Von David Ly und Thore Brehmer
from copy import deepcopy


#Findet das höchste xn herraus
def formel(xs):
    max = 1
    for x in xs:
        if (len(x)>max): max=len(x)
    return rek(xs,max)
    
  

def rek (xs,i):
    global Anzahl
    # Abbruch Bed
    if(i==0): return None
    for x in (i,-i):
        Anzahl +=1
        temp = deepcopy(xs)
        # print hilft beim Verstehen des codes
        # print("x =",x,"Liste =",temp)
        for term in xs:       
            # Löscht alle DisjunktionsTerme mit x
            if x in term: temp.remove(term)
            
        #Falls x bei 1 oder -1 angekommen ist.
        if(temp == []): return [x]
        #Rek. Aufruf
        loes =rek(temp,i-1) 
        if (loes!=None): return loes+[x]
        
    

 
        


test1 = [[1,2,3],[1,-2],[-1,-2,3],[-3]]
test2 = [[1,2,-3,-4,-5],[-5],[1],[-3,1]]
test3 = [[-1],[1]]

for test in (test1,test2,test3):
    Anzahl = 0
    print("Eingabe:",test,"Ergebnis:",formel(test),"Rekursionen:", Anzahl)