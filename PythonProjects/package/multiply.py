# My tools
# -*- coding:latin-1 -*
import os
def table(nb,max=12):
        i = 0
        while i <= max:
                print(nb," * ",i," = ",nb*i)
                i+=1
if __name__=="__main__" :
        table(9)
        os.system("pause")
