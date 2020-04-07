while True :
    name = input("Enter name ")
    datafile = open("Female.csv", encoding='utf-8')
    text = datafile.read().strip().split()
    datafile1 = open("Male.csv", encoding='utf-8')
    text1 = datafile1.read().strip().split()

    if name.lower() in text :
        print(name,'is girl')
    elif name.lower() in text1 :
        print(name, 'is boy')
    else : print("cant be determine ")
    datafile.close()
    datafile1.close()
    
