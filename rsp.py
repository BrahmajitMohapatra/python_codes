a=["Rock","Scissor","Paper"]
while True:
    i =input("Enter s to start game q to quit")
    if i== 'q' :
        break
    p1=input("Player 1 input ")
    p2=input("player 2 input")
    V1=a.index(p1)
    V2=a.index(p2)
    k=V1-V2
    if k == 0 :
        print("Same input Try again")
    elif k== -1 or k== 2:
        print("Congratulations !!!! Player 1 wins")
    else :
        print("Congratulations !!!! Player 2 wins")
     
     
