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