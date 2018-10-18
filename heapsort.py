import sys
from timeit import default_timer as timer

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

#HeapSort Function
#takes the list as parameters
#Takes the list and is the initial call to sort the list
#returns a sorted list
def heapSort(list):
	n = len(list) - 1
	buildMaxHeap(list)
	for i in range(n, 2, -1):
		list[1], list[i] = list[i], list[1]
		n = n - 1
		maxHeapify(list, 1)

#build Max Heapify Function
#takes the list as a parameter
#builds the heap in a max heap
def buildMaxHeap(list):
	n = len(list)
	for i in range((n // 2), 1, -1):
		maxHeapify(list, i)

#Max Heapify Function
#takes the list and index as parameters
#recursively calls itself to swap values into the right place
#returns a sorted list from the index
def maxHeapify(list, i):
	global call
	n = len(list) - 1
	left = 2 * i
	right = (2 * i) + 1
	if (left <= n) and (list[left] > list [i]):
		largest = left
	else :
		largest = i
	call = call + 2
	if (right <= n) and (list[right] > list[largest]):
		largest = right
	call = call + 2
	if largest is not i:
		list[i], list[largest] = list[largest], list[i]
		maxHeapify(list, largest)
	call = call + 1

#loop through the number of file arguments, open and then sort them
#must skip the first element in sys.argv, because it is the path of the file being executed
#returns nothing
#calls readFile and selectionSort functions
for item in sys.argv[1:]:
	list = readFile(item)
	n = len(list)

	start = timer()
	heapSort(list)
	end = timer()
	#output raw info: size, comparisons, and time
	print (str(n) + ', ' + str(call) + ', ' + str(end-start))
