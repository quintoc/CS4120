#import important libraries
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

#SelectionSort function
#takes the list from the file and selections sorts on it
#outputs the size of the list, the number of comaprisons and the tiem it took
#returns nothing
def selectionSort(list):
	start = timer()
	comparisons = 0
	n = len(list)
	for j in range(n-1):
		smallest = j
		i = j + 1
		for i in range(n):
			if list[i] < list[smallest]:
				smallest = i
			comparisons += 1
		list[j], list[smallest] = list[smallest], list[j]
	end = timer()
	time = end-start
	print(str(n) + ', ' + str(comparisons) + ', ' + str(time))

#loop through the number of file arguments, open and then sort them
#must skip the first element in sys.argv, because it is the path of the file being executed
#returns nothing
#calls readFile and selectionSort functions
for item in sys.argv[1:]:
	list = readFile(item)
	selectionSort(list)
