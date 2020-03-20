#!/usr/bin/env python3
#Assuine Jesen Chrichne

def add(a, b):
	return a + b
def main():
	import sys
	c = sys.argv
	if (len(c) != 3):
		
		print("Erreur : 2 argument seulement")
		a = input("Entrer le 1er nombre : ")
		b = input("Entrer le 2e nombre : ")

		print(add(eval(a),eval(b)))
		return		
	d = int(sys.argv[1])
	e = int(sys.argv[2])
	print(add(d,e))
	
	if (name =="_main_"):
		main()
	
main()
