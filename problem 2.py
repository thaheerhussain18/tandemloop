#user defined function to print series of numbers asked in test problem
def generateNumbers(a):
    output = []
    for i in range(1, a*2, 2):
        output.append(i)
    return output
            

a = int(input())
output = generateNumbers(a)
for i in output:
    print(i,end=',')
