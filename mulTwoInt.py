#!/usr/bin/env python3

#JOHANESA Asandratry Ny Avo
#multiplication 

def mul(a,b):
	return a*b


def main():
	import sys
	entre = sys.argv

	if (len(entre) != 3):
		print('Erreur : 2 arguments requis' )
		a = input('Entrez le premier nombre: ')
		b = input('Entrez le deuxieme nombre: ')

		try: #il arrive que input ne retourne pas une valeur "string" mais "int" (ex:Kali linux)
			print(mul(eval(a),eval(b))) 

		except:
			print(mul(a,b))
		return
	
	print(mul(eval(entre[1]),eval(entre[2])))

<<<<<<< HEAD

=======
>>>>>>> 109a5a4b500e15cfd8d2654e78ce157bce7cc3e7
if (__name__ == "__main__"):
	main()
	

