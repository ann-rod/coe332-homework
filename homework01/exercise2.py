# this program creates three lists: the first with ten integers, the second with
# the square of each integer, the third with the cube of each integer, and 
# prints the results.

def main():
	list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
	list2 = [ number**2 for number in list1 ]
	list3 = [ number**3 for number in list1 ]

	for i in range( len(list1) ):
		print( list1[i], list2[i], list3[i] )

main()
