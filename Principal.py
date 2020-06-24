import My_Lib
import numpy as np
import random


a = np.array(My_Lib.crea_algo(4,5)).reshape((4,5))
print(a)

y=4
while y>0:
    a = My_Lib.mueve_col(a,0)
    print(a)
    y-=1