from itertools import permutations
empt = []
ans = []

def solve(lists, budget):
    for a in reversed(range(0, len(lists) + 1)):
        subsets = list(permutations(lists, a))
    
        for b in subsets:
            if sum(b) <= budget:
                empt.append(b)
                break
            
      
    ans.append(len(empt[0]))
    empt.clear()
    
  

test = int(input())
for i in range(test):
    query = [int(x) for x in input().split()]
    cases = [int(y) for y in input().split()]
    solve(cases, query[1])
    
    

for z in range(len(ans)):
    print("Case #" + str(z+1) + ":", ans[z])
