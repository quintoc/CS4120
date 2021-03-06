#import important libraries
import sys
from timeit import default_timer as timer


#Have to set higher recursion limit for pyhton than default
sys.setrecursionlimit(100000)

#list all the files that are being sorted
print ('sys.argv is', sys.argv)
#set number of comparisons variable
call = 0

#function that recieves file path and opens
#then reads in all the lines into a list
#returns the list
def readFile(fileName):
	list = []
	file = open(fileName, 'r')
	for line in file:
		line = line.strip()
		list.append(int(line))
	return list

#Quick Sort Function
#take the list, start and end values as parameters
#partiions the list, then recursively calls itself until list is sorted
#returns a sorted list
def quickSort(list, p, r):
	global call
	if (p < r):
		middle = partition(list, p, r)
		quickSort(list, p, (middle - 1))
		quickSort(list, (middle + 1), r)
	call = call + 1

#Partition Function
#takes the list, start and end variables as parameters
#finds the middle of the list so that quick sort function can operate properly
#returns the index of the desired split
def partition(list, start, end):
	global call
	last = list[end]
	i = start - 1
	for j in range(start, end - 1):
		if list[j] <= last:
			i = i + 1
			list[i], list[j] = list[j], list[i]
		call = call + 1
	list[i + 1], list[end] = list[end], list[i + 1]
	return (i + 1)


#loop through the number of file arguments, open and then sort them
#must skip the first element in sys.argv, because it is the path of the file being executed
#returns nothing
#calls readFile and selectionSort functions

for item in sys.argv[1:]:
	list = readFile(item)
	begin = 0
	n = len(list)

	start = timer()
	quickSort(list, begin, n - 1)
	end = timer()
	#raw output of size, comparisons, and time function took
	print(str(n) + ', ' + str(call) + ', ' + str((end-start)))

