empt = []

def solve(f, l):
    count = 0
    for a in range(f, l + 1):
        if a % 9 != 0 and "9" not in str(a):
            count += 1
    
    empt.append(count)


            
                
test = int(input())
for i in range(test):
    cases = [int(x) for x in input().split()]
    solve(cases[0], cases[1])

for j in range(len(empt)):
    print("Case #" + str(j+1) + ":", empt[j])
