def generateNumbers(a):
    if(a%2==0):
        a-=1
    output = []
    for i in range(1, a*2, 2):
        output.append(i)
    return output
            

a = int(input())
output = generateNumbers(a)
for i in output:
    print(i,end=',')
