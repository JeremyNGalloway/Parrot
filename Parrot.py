#Jeremy Galloway JeremyNGalloway@gmail.com
#This simple python module echos the source code of the program it's being called from.
#Implement via a "--source" argument, for example
#http://en.wikipedia.org/wiki/Quine_%28computing%29

import sys

source = sys.argv[0]
code = open(source,'r')

print code.read()

code.close()
	
