from itertools import combinations
empt = []

def solve(l):
    count = 0
    comb = list(combinations(l, 3))
    for i in comb:
        if i[0] == i[1] * i[2]:
            count += 1
            continue
            
        if i[1] == i[0] * i[2]:
            count += 1
            continue
        
        if i[2] == i[1] * i[0]:
            count += 1
            continue
    
    empt.append(count)


test = int(input())
for a in range(test):
    qry = int(input())
    cases = [int(x) for x in input().split()]
    solve(cases)

for b in range(len(empt)):
    print("Case #" + str(b+1) + ":", empt[b])
        
        
