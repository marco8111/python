def elemento_matriz(mat,linha,col):
    if linha > len(mat) - 1:
        print("indice de linha invalido :",linha)
    elif col > len (mat[0]) -1 :
        print ("indice invalido : ",col)
    else :
        return mat[linha] [col]
m = [[1,2,3],[4,5,6]]
print(elemento_matriz(m,0,2))
