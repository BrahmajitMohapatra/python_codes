import json
neow = open("nasa.json")
data = json.load(neow)
neow.close()
#print(data)
lst=[]
dta=[]
for a,b in data.items():
    lst.append(a)
    dta.append(b)

for k,v in dta[2].items():
    for i in v:
        for x,y in i.items():
            print("\n\n\n\n  data \n\n\n")
            print(x,y)
            for i in y:
                print(i)
            
