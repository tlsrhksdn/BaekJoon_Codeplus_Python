def digit(n):
    num=1
    while(n<10):
        n=n//10
        num+=1
    return num

N=int(input())

count=0

while N!=0:
    count+=digit(N)
    N-=1
    
print(count)

