def crea_algo(f,c):
    import random               #f=num de filas
    Matriz=[]                   #c=num de columnas
    #Creacion de el arreglo                   
    for i in range(f):
        Matriz.append([0]*c)                       
    
    for i in range(f):
        for j in range(c):
            Matriz[i][j]=random.randint(1,100)

    return Matriz

def mueve_col(M,i):
    import numpy as np
    Array_colum = M[0,i:(i+1)]
    Array_sincolum = np.delete(M,i,axis=1)
    #para insertar
    Array_sincolum = np.insert(Array_sincolum, Array_sincolum.shape[1], Array_colum, axis=1)
    return Array_sincolum

