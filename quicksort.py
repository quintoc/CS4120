import sys
from timeit import default_timer as timer

#Have to set higher recursion limit for pyhton than default
sys.setrecursionlimit(100000)
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

#Quick Sort Function

def quickSort(list, p, r):
	if (p < r):
		middle = partition(list, p, r)
		quickSort(list, p, (middle - 1))
		quickSort(list, (middle + 1), r)

def partition(list, start, end):
	last = list[end]
	i = start - 1
	for j in range (end - 1, start, 1):
		if list[j] <= last:
			i = i + 1
			list[i]. list[j] = list[j], list[i]
	list[i + 1], list[end] = list[end], list[i + 1]
	return (i + 1)


#loop through the number of file arguments, open and then sort them
#must skip the first element in sys.argv, because it is the path of the file being executed
#returns nothing
#calls readFile and selectionSort functions
for item in sys.argv[1:]:
	list = readFile(item)
	start = 0
	n = len(list)
	quickSort(list, start, n - 1)
	#print(list)
