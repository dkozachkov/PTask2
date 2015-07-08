import sys, math

try:
    outfilename = sys.argv[1]
except:
    print "Usage",sys.argv[0],"infile outfile" # not enough args  
ofile = open(outfilename, 'w')  #open file, write-mode

def myfunc(y):
    if y>=0.0:
        return y ** 5*math.exp(-y)    # ** - raise to power
    else:
        return 0.0
    
i=2
while i <= len(sys.argv)-1:
    x = float(sys.argv[i])
    y = float(sys.argv[i+1])
    fy = myfunc(y)
    ofile.write('%g %12.5e\n' % (x,fy))
    # write x and f(y)
    i+=2
        
ofile.close()