import My_Lib
import numpy as np
import random


a = My_Lib.crea_algo(20,20)
a = np.reshape((4,5))
print(a)

y=4
while y>0:
    a = My_Lib.mueve_col(a,0)
    print(a)
    y-=1