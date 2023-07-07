"""
Stückweise konstante Funktionen,
dargestellt durch ein Tupel ungerader Länge

  F = (a0,h1,a1,h2,a2, .... ,h_n,a_n)

Für a_(i-1)<=x<a_i gilt: F(x)=h_i
Außerhalb des Intervalls a_0<=x<a_n ist F(x) nicht definiert.

"""

############################################Von hier######################################################################
def verschiebe (F,b):
    liste = []
    for i in range(0, len(F)):
        if i % 2 == 0:
            liste = liste + [F[i]-b]
        else:
            liste = liste + [F[i]]
    return liste

#Vorbedienung. Die Funktionen besitzen keine Definitionslücken. Die Eingabe Funktionen sind aufsteigend definiert
def fallunterscheidung (b,F,G):
    liste = []
    if b>F[0]:
        for i in range(0,len(F),2):
            if b<F[i]:
                liste = list(G[:i]) + [b] + [None]
                break

    for i in range(0,len(G),2):
        if b <= G[i]:
            liste = liste + list(G[i:]) 
            break
    return tuple(liste)

#tests
F1 = (0,2,3,1,5,5,10)
G1 = (1,-4,3,8,11)

print("F=",F1)
print("G=",G1)

print("Fallunterscheidung(2 F G):",fallunterscheidung(2,F1,G1))
print("Verschiebe(F 1):",verschiebe(F1,1))

print()
print()



##############################################bis hier####################################################################

def berechne(F,x):
    if x<F[0] or x>=F[-1]: return None
    i=0
    while x>=F[i]: i+=2
    return F[i-1]

def add(F,G):
    return tuple(_add(F,G))

def _add(F,G): # Generatorfunktion
    yield max(F[0],G[0])
    i = j = 0
    while True:
        nächsterSprung = min(F[i],G[j])
        if i>0 and j>0:
            yield F[i-1]+G[j-1] # Funktionswert
            yield nächsterSprung
        if F[i]==nächsterSprung:
            if i==len(F)-1: return
            i+=2
        if G[j]==nächsterSprung:
            if j==len(G)-1: return
            j+=2

F1 = (0,2,3,1,5,5,10)
G1 = (1,-4,3,8,11)
H1 = add(F1,G1)

print("2F ",add(F1,F1))
print(" F ",F1)
print(" G ",G1)
print("F+G",H1)

print("\n     x  F(x)  G(x) F(x)+G(x)")
for i in range(-2,13):
    x = i + 0.5
    print ((" %5s"*4)%(x,berechne(F1,x),berechne(G1,x),berechne(H1,x)))
