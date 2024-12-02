def read_input_lists(file):
	list1 = [], list2 = []
	with open(file, 'r') as f:
		for line in f:
			first, second = line.split()
			list1.append(int(first))
			list2.append(int(second))
	return list1, list2

def find_distance(list1, list2):
	return sum([abs(x - y) for x, y in zip(list1, list2)])

def find_similarity(list1, list2):
	similarity = 0
	cache = {}
	for i in range(len(list1)):
		if list1[i] not in cache:
			cache[list1[i]] = list2.count(list1[i])
		similarity += cache[list1[i]] * list1[i]
	return similarity

def main():
	list1, list2 = read_input_lists('input')
	list1.sort()
	list2.sort()
	print(find_distance(list1, list2))
	print(find_similarity(list1, list2))

if __name__ == '__main__':
	main()
