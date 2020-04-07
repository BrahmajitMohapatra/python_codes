def checkMatrix(w, h, Matrix):
    flag = True
    count = tmpcnt = 0
    #print(Matrix)
    while flag:
        for i in range(0, w):
            for j in  range(0, h):
                if (i == 0 or j == 0) or (i == w - 1 or j == h - 1):
                    pass#print(".")
                else:
                    endtoend = min(Matrix[i][0], Matrix[i][h-1])
                    #print(endtoend, Matrix[i][0], Matrix[i][h-1])
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
    print("\n", count, Matrix)
    return count

def GetWaterLevel(input1,input2,input3):
    global flag
    w, h = input1, input2
    count = 0
    newList = []
    Matrix = [input3[i:i+h] for i in range(0, len(input3), h)]
    return checkMatrix(w, h, Matrix)


GetWaterLevel(3, 6, [3, 3, 4, 4, 4, 2,   3, 1, 3, 2, 1, 4,   7, 3, 1, 6, 4, 1])
