from copy import deepcopy

def test_straight(xs,y,x,n):
    for i in range(0,n):
        if(xs[y][i]==True and i!=x): return False
        if(xs[i][x]==True and i!=y): return False
    return True
    
def test_diag(xs,y,x,n):
    max = (n-1)

    x2,y2=x-1,y-1
    while(x2>=0 and y2>=0):
        if(xs[y2][x2]==True): return False
        x2 -=1
        y2 -=1
        
    x2,y2=x-1,y+1
    while(x2>=0 and y2<=max):
        if(xs[y2][x2]==True): return False
        x2 -=1
        y2 +=1
        
    x2,y2=x+1,y-1
    while(x2<=max and y2>=0):
        if(xs[y2][x2]==True): return False
        x2 +=1
        y2 -=1
        
    x2,y2=x+1,y+1
    while(x2<=max and y2<=max):
        if(xs[y2][x2]==True): return False
        x2 +=1
        y2 +=1
        
    return True
               
def test_horse(xs,y,x,n):
    max = n-1
    poslb =[(y-2,x+1),(y-2,x-1),(y+2,x+1),(y+2,x-1),(y+1,x+2),(y-1,x+2),(y+1,x-2),(y-1,x-2)]
    for i in poslb:
        if(i[0]>=0 and i[1]>=0 and i[0]<=max and i[1]<=max and xs[i[0]][i[1]] == True): return False
    return True
               
def drache(xs,n, count):
    
    for y in range(0,n):
        for x in range(0,n):
            if(test_straight(xs,y,x,n)==True and ((y,x) not in count) and test_diag(xs,y,x,n) and test_horse(xs,y,x,n)):
                temp = deepcopy(xs)
                temp[y][x] = True
                print (drache(temp, n, count+[(y,x)]))
                   
    return count
        
def teste_drache(n):
    xs = [[False for i in range(0,n)] for i in range(0,n)] 
    print(drache(xs,n,[]))
        
teste_drache(8)       
        
        