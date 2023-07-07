#Aufgabe 59
def f(t):
    faecher = [0 for i in range(0,1024)]
    
    for i in range(0,1024):
        faecher[(t*i)%1024] +=1
        
    max = faecher[0]
    for x in faecher:
        if (x>max): max=x
        
    return max

#  experiment
for t in [0,1,2,3,4,5,13,20]:
    print("t=",t," max=",f(t))
    print()
