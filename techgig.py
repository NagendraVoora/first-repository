n=int(input())

def check(k):
    string=str(k)
    print("value:"+string)
    if (string.find("2")==-1) and (string.find("14")==-1):
        print(1)
        return 1
    else:
        print(0)
        return 0
    
count=0
i=1
while count<n:
    if check(i):
        count+=1
    else:
        count=count
    i+=1
    print("count is"+str(count))
print(i-1)
