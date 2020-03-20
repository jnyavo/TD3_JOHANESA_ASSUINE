#!/usr/bin/env python3

def mul(a,b):
	return a*b


def main():
	import sys
	entre = sys.argv

	if (len(entre) != 3):
		print('Erreur : 2 arguments requis' )
		a = input('Entrez le premier nombre: ')
		b = input('Entrez le deuxieme nombre: ')
		try:
			print(mul(a,b))
		except:
			print(mul(eval(a),eval(b)))		
		return
	
	print(mul(eval(entre[1]),eval(entre[2])))

main()
	

