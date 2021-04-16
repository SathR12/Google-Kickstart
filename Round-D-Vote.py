empt = []
def solve(n, m):
    empt.append((n-m) / (n+m))
    


test = int(input())
for i in range(test):
    cases = [int(x) for x in input().split()]
    solve(cases[0], cases[-1])
    
for j in range(len(empt)):
    print("Case #" + str(j+1) + ":", empt[j])
