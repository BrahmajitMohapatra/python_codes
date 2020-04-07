def isPrime(a=0):
    i=2
    if a==0 :
        return 0
    while(i<a):
        if a%i==0:
            return 0
        i=i+1
    return 1
x=int(input("Enter The number : "))
if(isPrime(x)):
    print(x, "is Prime number ")
else :
    print(x," is not Prime number")
