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
Mat = [Mat1[i] for i in range(1,w+1)]
Matrix=[list(map(int,row)) for row in Mat]
print(Matrix)
