import pickle
data=[['scott',7788,3000.00],
      ['blake',7902,2500.00],
      ['smith',7369,4000.00]]
x=None
try :
    x=open("picfile.txt","wb")
    print("file is opened ")
    pickle.dump(data,x)
except:
    print("Error occured ")
finally :
    if x!=None:
        x.close()
        print("file closed")
