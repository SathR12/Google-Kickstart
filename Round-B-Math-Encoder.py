from itertools import combinations
caser = []

def solve(l):
    empt = []
    for i in range(1, len(l) + 1):
        combs = list(combinations(l, i))
        
        for j in combs:
            if len(j) > 1:
                empt.append(max(j) - min(j))
            
            
                
    caser.append(sum(empt) % 1000000007)
    
                

test = int(input())

for a in range(test):
    query = int(input())
    cases = [int(x) for x in input().split()]
    solve(cases)

for b in range(len(caser)):
    print("Case #" + str(b+1) + ":", caser[b])
