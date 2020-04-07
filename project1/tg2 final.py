#import numpy as np

def main():
    flag = True
    count = tmpcnt = 0
    l=raw_input()
    #print(l)
    l1=[]
    l1=l.split(" ")
    w=int(l1[0])
    h=int(l1[1])

    mat = []
    for i in range(w):
        mat.append(raw_input())
    print(mat)

    Mat1 =[[]]
    for i in range(w):
        Mat1.append(mat[i].split())
    Mat= [Mat1[i] for i in range(1,w+1)]
    Matrix=[list(map(int,row)) for row in Mat]
    

    print(Matrix)
    while flag:
        for i in range(0, w):
            for j in  range(0, h):
                
                if (i == 0 or j == 0) or (i == w - 1 or j == h - 1):
                    pass
                else:
                    endtoend = min(Matrix[i][0], Matrix[i][h-1])
                    
                    uptodown = min(Matrix[i-1][j], Matrix[i+1][j])
                    leftright = min(Matrix[i][j-1], Matrix[i][j+1])
                    newList = [Matrix[i-1][j], Matrix[i][j-1], Matrix[i+1][j], Matrix[i][j+1]]

                    minval = min(newList)
                    if minval > Matrix[i][j]:
                        Matrix[i][j] += 1
                        count += 1
                    elif endtoend > Matrix[i][j]:
                            
                            if w < h:
                                if endtoend == Matrix[i][j] + 1:
                                    Matrix[i][j] += 1
                                    count += 1
                            else:
                                if Matrix[i-1][j] > Matrix[i][j]:
                                    Matrix[i][j] += 1
                                    count += 1

                       
                if tmpcnt == count and i == w - 1 and j == h - 1:
                    flag = False
        tmpcnt = count
    print(count)
main()


