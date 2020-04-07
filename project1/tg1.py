import numpy as np

def checkMatrix(w, h, Matrix):
    flag = True
    count = tmpcnt = 0
    #print(Matrix,w,h)
    while flag:
        for i in range(0, w):
            for j in  range(0, h):
                if (i == 0 or j == 0) or (i == w - 1 or j == h - 1):
                    pass
                else:
                    endtoend = min(Matrix[i][0], Matrix[i][h-1])
                    #print(endtoend, Matrix[i][0], Matrix[i][h-1])
                    #print("i=",i," j=",j)
                    uptodown = min(Matrix[i-1][j], Matrix[i+1][j])
                    leftright = min(Matrix[i][j-1], Matrix[i][j+1])
                    newList = [Matrix[i-1][j], Matrix[i][j-1], Matrix[i+1][j], Matrix[i][j+1]]

                    minval = min(newList)
                    if minval > Matrix[i][j]:#Matrix[i][j] < endtoend and Matrix[i][j] < uptodown:# and
                        Matrix[i][j] += 1
                        count += 1
                    elif endtoend > Matrix[i][j]:
                            #if i-1 != 0 and j-1 != 0 and i+1 != w - 1 and j-1 != h - 1:
                            if w < h:
                                if endtoend == Matrix[i][j] + 1:
                                    Matrix[i][j] += 1
                                    count += 1
                            else:
                                if Matrix[i-1][j] > Matrix[i][j]:
                                    Matrix[i][j] += 1
                                    count += 1

                        # if h > w and uptodown > Matrix[i][j]:
                        #     Matrix[i][j] += 1
                        #     count += 1
                        #
                        # else:#if w >= h and uptodown > Matrix[i][j]:
                        #     Matrix[i][j] += 1
                        #     count += 1
                if tmpcnt == count and i == w - 1 and j == h - 1:
                    flag = False
        tmpcnt = count
    print(count)
    return count

def GetWaterLevel():
    l=raw_input()
    print(l)
    l1=[]
    l1=l.split(" ")
    w=int(l1[0])
    h=int(l1[1])

    mat = np.zeros((w,h))
    for i in range(w):
        mat[i]=raw_input().split(" ")
    print(mat)
    return checkMatrix(w, h, mat)

GetWaterLevel()
#GetWaterLevel(4, 6, [3, 3, 4, 4, 6, 2,   3, 1, 3, 6, 1, 6,   7, 3, 1, 6, 6, 1])

