# testexample=[1,2,8,9,12,46,76,82,15,20,30]
val=list(map(int,input().split()))
dic={}
for i in range(1,10):
    c=0
    for j in val:
        if(j%i==0):
            c+=1
    dic[i]=c
print(dic)

