x=open("myfile.txt")
lines = x.readlines()
for p in lines :
    print(p,end=" ")
x.close()
