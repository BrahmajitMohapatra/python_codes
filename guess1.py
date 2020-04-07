import random
while True:
    j=0
    a = random.randint(0, 9)
    while True:
        i=int(input("Enter your Guess = "))
        j=j+1
        if i < a :
            print("Number is too small ")
        elif i > a :
            print("Number is too large ")
        else :
            print("Congratulation!!!! you guessed correct ")
            break
    print("Guess count ",j)
    if(input("Please type exit to leave the game or enter :")=='exit'):
        break

