#Lauft den Binaerbaum rekursiv ab
def MWeg (xs, m=0,i=1):
    Llen = len(xs)-1
    #Untersucht ob linkes UND rechtes Kind existiert
    if (left(i)<=Llen and right(i)<=Llen):
        if (xs[left(i)]!=None and xs[right(i)]!=None ):
            return float(m)/xs[0] + MWeg(xs,m+1,left(i)) + MWeg(xs,m+1,right(i))
        elif(xs[left(i)]!=None):
            return float(m)/xs[0] + MWeg(xs,m+1,left(i))
        elif(xs[right(i)]!=None):
            return float(m)/xs[0] + MWeg(xs,m+1,right(i))
    #Untersucht ob linkes Kind existiert
    elif (left(i)<=Llen):
        if(xs[left(i)]!=None):
            return float(m)/xs[0] + MWeg(xs,m+1,left(i))
    #Untersucht ob rechtes Kind existiert
    elif (right(i)<=Llen):
        if(xs[right(i)]!=None):
            return float(m)/xs[0] + MWeg(xs,m+1,right(i))
    return float(m)/xs[0]
    
def parent(i):
    return i//2
def left(i):
    return i*2
def right(i):
    return i*2+1
    

#Test Funktionen
xs = [3,2,1,3]
ys = [6,5,4,6,2,5,None,7]
zx = [4,10,None,11,None,None,None,13,None,None,None,None,None,None,12]
print("MWeg(",xs,") = ",MWeg(xs))
print("MWeg(",ys,") = ",MWeg(ys))
print("MWeg(",zx,") = ",MWeg(zx))