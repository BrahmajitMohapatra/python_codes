import csv

name = input("Enter your name ")

with open("Female.csv",'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader :
                for field in row :
                        if field == name:
                                print(name,"is girl")
                                break
                
        else : print("not found")
                        
