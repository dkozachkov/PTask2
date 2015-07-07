import random

n=100000
counter=0;
for i in range(1,n):
    s1=int(random.randrange(6))+1
    s2=int(random.randrange(6))+1
    if s1==6 or s2==6:
        counter+=1
res=float(counter)/n
print '{:.3}'.format(res)