import sys

try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print "Usage",sys.argv[0],"infile outfile"   
ifile = open(infilename, 'r')
ofile = open(outfilename, 'w')

for line in ifile:
    pars = line.split()
    summ=0
    n=len(pars)
    for j in range(0,n):
        x = float(pars[j])
        ofile.write('%12.6f ' %x)
        summ+=x
    ave=float(summ)/n
    ofile.write('%12.6f\n' %ave)
        
ifile.close()
ofile.close()