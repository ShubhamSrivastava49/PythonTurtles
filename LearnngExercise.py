
l=[]

for i in range(200,320):
    
    if ( i%7==0 and i%5!=0):  

          l.append(str(i))

    print ",".join(l)


