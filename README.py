# immortal
# dump calculator v1
from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.GREEN)
print( Back.YELLOW)
what = input( " what doing? (+ , - )")
print( Back.RED)
a =float(  input("write first letter:"))
b =float( input("write second letter:"))
print( Back.CYAN)
if what == "+":
	c = a + b
	print("result " + str (c) )
elif what == "-":
	c = a - b 
	print("result " + str (c) )
else:
	print("chose wrong operation!")
	test3.py
input("did you like it? :)")