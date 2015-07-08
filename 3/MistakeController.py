import sys, random
def compute(n):
    i = 0; s = 0
    while i <= n:
        s += random.random()
        i+=1
    return s/n

n=sys.argv[1]
print 'average of %d random numbers is %f' %(int(n),compute(n))