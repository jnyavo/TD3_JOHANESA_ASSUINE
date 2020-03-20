#!/usr/bin/env python3
def add(a, b):
	return a + b
def main():
	import sys
	c = sys.argv
	d = int(sys.argv[1])
	e = int(sys.argv[2])
	print(add(d,e))
main()
