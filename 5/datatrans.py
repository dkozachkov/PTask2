import sys, math

try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print "Usage",sys.argv[0],"infile outfile" # not enough args  
ifile = open(infilename, 'r')   #open file, read-mode
ofile = open(outfilename, 'w')  #open file, write-mode

def myfunc(y):
    if y>=0.0:
        return y ** 5*math.exp(-y)    # ** - raise to power
    else:
        return 0.0
    
for line in ifile:
    pair = line.split()
    x = float(pair[0])  #string must contain 2 float numbers
    y = float(pair[1])
    fy = myfunc(y)
    ofile.write('%g %12.5e\n' % (x,fy))
    # write x and f(y)
        
ifile.close()
ofile.close()