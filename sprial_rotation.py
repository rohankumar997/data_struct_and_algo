def Sprial_Rotation_arry(mat, m, n):
    dir=0
    T=0
    B=m-1
    L=0
    R=n-1
    counter=0
    while(T<=B and L<=R and counter<=m*n):
        if(dir==0):
            for i in range(L,R+1):
                print(mat[T][i],end=" ")
            T+=1
            dir=1
    
        if(dir==1):
            for i in range(T,B+1):
                print(mat[i][R],end=" ")
            R-=1
            dir=2

        if(dir==2):
            for i in range(R,L-1,-1):
                print(mat[B][i],end=" ")
            B-=1
            dir=3

        if(dir==3):
            for i in range(B,T-1,-1):
                print(mat[i][L],end=" ")
            L+=1
            dir=0
        counter+=1


Sprial_Rotation_arry([[1, 2, 3, 4, 5, 6],
                             [7, 8, 9, 10, 11, 12],
                             [13, 14, 15, 16, 17, 18]], 3, 6)


