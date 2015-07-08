import sys, math

def get_answer(arg):
    try:
        x=math.log(float(arg))
    except:
        return 'is illegal'
    return x

#while i<len
i=1
while 1:
    try:
        r = sys.argv[i]
    except:
        break
    s = get_answer(r)
    print 'ln(%f) = ' %float(r),s
    i+=1