def solve():
    count = 0
    empt = []
    test = int(input())
    for i in range(test):
        query = input()
        cases = [int(x) for x in input().split()]
        
        for j in range(len(cases)):
            if j == 0 or j == len(cases) - 1:
                continue
            elif cases[j-1] < cases[j] > cases[j+1]:
                count += 1
        empt.append(count)
        count = 0
            
        
    for a in range(len(empt)):
        print("Case #" + str(a+1) + ":", empt[a])
        
solve()
