def is_boring(inp):
    count = 0
    for x,y in enumerate(inp):
        #print(x,y)
        npn = x + 1
        np = str(npn)
        if (np in odd and y in odd):
            count = 1
            continue
        elif (np in even and y in even):
            count = 1
            continue
        else:
            count = 0
            break
        
        
        
    return count

    



odd="13579"
even="02468"
total = 0
empt = []

test = int(input())
for j in range(test):
    cases = [int(x) for x in input().split()]
    total = 0
    start = cases[0]
    end = cases[1] + 1
    for i in range(start,end):
        count = is_boring(str(i))
        total = total + count
    empt.append(total)


for a in range(len(empt)):
    print("Case #" + str(a+1) + ":", empt[a])
    
