def fibo(x):
    if x == 1 or x == 2:
        return 1
    return (fibo(x-1)+fibo(x-2))

def userinput(y):
    i=1
    while(i <= y):
        print(fibo(i),end=" ")
        i=i+1

z=int(input("enter the number of sequence :"))
userinput(z)
