import sys, math

def get_answer(arg):
    try:
        x=math.log(float(arg))
    except:
        return 'is illegal'
    return x

#for in range
for i in range(1,len(sys.argv)):
    r = sys.argv[i]
    s = get_answer(r)
    print 'ln(%f) = ' %float(r),s