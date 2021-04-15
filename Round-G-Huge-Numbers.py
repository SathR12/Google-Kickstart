import math

def solve():
    test = int(input())
    empt = []
    caser = []
    
    for i in range(0, test):
        cases = [int(x) for x in input().split()]
        empt.append(cases)
     
    for j in empt:
       fact = math.factorial(j[1])
       case = j[0] ** fact % j[2]
       caser.append(int(case))
       
            
        
        
        
    

    for a in range(0, test):
        print("Case #" + str(a+1) + ":", caser[a])


solve()
