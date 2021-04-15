from itertools import combinations
empt = []

def solve(l, r):
    count = 0
    for i in range(2, r + 1):
        subarrays = set(combinations(l, i))
        for j in subarrays:
            if sum(j) >= 0:
                if pow(sum(j), .5) == int(pow(sum(j), .5)):
                    count += 1
            
    for k in l:
        if k >= 0:
            if pow(k, .5) == int(pow(k, .5)):
                count += 1
                
            
    
    
    empt.append(count)
        



test = int(input())
for a in range(test):
    query = int(input())
    cases = [int(x) for x in input().split()]
    solve(cases, query)

for b in range(len(empt)):
    print("Case #" + str(b+1) + ":", empt[b])
    
