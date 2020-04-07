import pickle
with open ("picfile.txt","rb") as x:
    data=pickle.load(x)
    for p in data:
        print(p)
        
