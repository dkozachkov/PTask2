import random

n=100000
counter=0;
for i in range(1,n):
    s1=int(random.randrange(6))+1
    if s1>5:
        continue
    s1+=int(random.randrange(6))+1
    if s1>6:
        continue
    s1+=int(random.randrange(6))+1
    if s1>7:
        continue
    s1+=int(random.randrange(6))+1
    if s1<9:
        counter+=1
res=float(counter)/n
print '{:.3}'.format(res)