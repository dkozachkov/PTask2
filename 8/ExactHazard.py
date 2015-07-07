counter=0; total=0
print "Absolute value:"
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                if i+j+k+l<9:
                    counter+=1;
                total+=1;
print counter,"/",total,"\n",float(counter)/total