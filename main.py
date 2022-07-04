import sympy
import xlwings

import sympy as sympy
from sympy import summation, oo, symbols, log, var
i,j = symbols ('i j', integer=True)

c=[1,2,3,6,6,8]
print(c[2])
#for i in range(1,5):
    #for j in range (1,i-2):
        #eq1 = summation((2 * c[i]) - j , (j, 1, i - 2)) # j is worked as number even with difinition as sympols
        #print (i,j)
eq2 = summation(2 * i - 1, (i, 1, j))
        #eq2 = summation((2 * i) - j , (i, 1, 2)) # j as limits is not applicable for list while i is itrable and could apply for list
        #for j in range (1,i-1 ):
        #eq3 = (c [i]) - (c[j] ) # works ok
        #eq4= sum(2 * c[i]) - c[j]*1) # j as limits is not applicable for list while i is itrable and could apply for list
print (eq2)
