#!/usr/bin/env python3

def mul(a,b):
	return a*b


def main():
	import sys
	entre = sys.argv
	print(mul(eval(entre[1]),eval(entre[2])))
main()
	

