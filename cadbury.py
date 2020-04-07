''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    M = int(input())
    N = int(input())
    P = int(input())
    Q = int(input())
    total =0;
    if M<=N and P<=Q and P>0 and Q>0 and M>0 and N>0 :
        for row in range(M,N+1):
            for column in range(P,Q+1):
                rem_row=row
                rem_column=column
                
                while(rem_row!=0 and rem_column!=0):
                    if rem_row==rem_column:
                        total= total+1
                        rem_row=0
                        rem_column=0
                    elif rem_row > rem_column:
                        rem_row = rem_row-rem_column
                        total=total+1
                    elif rem_column > rem_row:
                        rem_column = rem_column - rem_row
                        total = total +1
    print total  
 # Write code here 

main()

