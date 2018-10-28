# -*- encode:latin-1 -*
# A test program for my fonctions
import os
from package.multiply import table
number = input("Enter the number of which you want to get the table\n")
number = int(number)
table(number)
os.system("pause")
