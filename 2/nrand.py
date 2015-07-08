import random
import sys

summ=0
n=int(sys.argv[1])
print "Numbers:"
for i in range(0,n):
    r = random.random() * 2 - 1
    summ+=r
    print '{:.4}'.format(r)
print "Average =",summ/n