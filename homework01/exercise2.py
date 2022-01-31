# this program prints three lists: the first with ten integers, the second with
# the squares of the integers in list 1, the third with the cubes of the
# integers in list 1.

def main():
	list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
	list2 = [ number**2 for number in list1 ]
	list3 = [ number**3 for number in list1 ]

	for i in range( len(list1) ):
		print( list1[i], list2[i], list3[i] )

main()
