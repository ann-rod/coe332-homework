# this program creates a list of integers, determines if each integer is even or 
# odd, and prints the results.

def evenOrOdd( integer ):
	if( integer % 2 == 0):
		status = 'even'
	else:
		status = 'odd'
	return status

def main():
	integers = [ x for x in range(10) ]
	for i in range( len(integers) ):
		status = evenOrOdd( integers[i] )
		print( integers[i], status )

main()
