import sys, math

def get_answer(arg):
    try:
        x=math.log(float(arg))
    except:
        return 'is illegal'
    return x

#while i<len
i=1
while (i<len(sys.argv)):
    r = sys.argv[i]
    s = get_answer(r)
    print 'ln(%f) = ' %float(r),s
    i+=1