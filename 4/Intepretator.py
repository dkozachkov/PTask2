import sys, math

def get_answer(arg):
    try:
        x=math.log(float(arg))
    except:
        return 'is illegal'
    return x

#for in sys
for r in sys.argv[1:]:
    s=get_answer(r)
    print 'ln(%f) = ' %float(r),s