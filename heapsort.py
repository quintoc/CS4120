import sys
from timeit import default_timer as timer

#list all the files that are being sorted
print ('sys.argv is', sys.argv)

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
def heapSort(list):
	n = len(list)
	buildMaxHeap(list)
	for i in range(n, 2, -1):
		list[1], list[i] = list[i], list[1]
		n = n - 1
		maxHeapify(list, 1)



def buildMaxHeap(list):
	n = len(list)
	for i in range((n // 2), 1, -1):
		maxHeapify(list, i)

def maxHeapify(list, i):
	n = len(list)
	left = 2 * i
	right = (2 * i) + 1
	if (left <= n) and (list[left] > list [i]):
		largest = left
	else :
		largest = i
	if (right <= n) and (list[r] > list[largest]):
		largest = r
	if largest is not i:
		list[i], list[largest] = list[largest], list[i]
		maxHeapify(list, largest)


#loop through the number of file arguments, open and then sort them
#must skip the first element in sys.argv, because it is the path of the file being executed
#returns nothing
#calls readFile and selectionSort functions
for item in sys.argv[1:]:
	list = readFile(item)
	heapSort(list)
	#print(list)
