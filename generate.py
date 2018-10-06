import random
max = 1000001
sizes = [20000, 40000, 80000, 160000]
types = ['random', 'sorted', 'rsorted', 'same']

def generateFile (type, size):
	list = random.sample(range(max), size)
	randomNum = list[0]
	if type == 'same':
		for i in range(len(list)):
			list[i] = randomNum
	elif type == 'sorted':
		list.sort()
	elif type == 'rsorted':
		list.sort(reverse=True)


	file = open(type + str(size) + '.txt', 'w')
	for item in list:
		file.write(str(item) + '\n')
	file.close()

for type in types:
	for size in sizes:
		generateFile(type,size)
