#My first Python program afetr 4 years of inactivity
# Bissextile year detector

# -*-coding:Latin-1 -*
from os import system

year = int(input("Please type in the year\n"))
rest = year%4
isBissextile = False
if rest != 0 : # Checking divisibility by 4;
	isBissextile = False
else :
	dividedBy100 = year%100 
	if dividedBy100 != 0 : # Now checking divisibilty by 100;
		isBissextile = True
	else : # In case the number is multiple of 100; we have to check if is it multiple of 400;
		dividedBy400 = year%400
		if dividedBy400 != 0 :
			isBissextile = False
		else :
			isBissextile = True
status = ''
if isBissextile :
	status = "bissextile"
else :
	status = "not bissextile"
print("year {0} is {1}".format(year,status))
system("pause")
