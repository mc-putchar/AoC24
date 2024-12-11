def read():
	equations = []
	with open('input', 'r') as f:
		for line in f:
			value, numbers = line.split(':')
			equations.append((int(value), [int(n) for n in numbers.strip().split()]))
	return equations

def operate(nums, ops):
	res = nums[0]
	op = 1 << (len(nums) - 2)
	for num in nums[1:]:
		res = (res * num) if ops & op else (res + num)
		op >>= 1
	return res

def is_possible(eq):
	val, nums = eq[0], eq[1]
	for ops in range(1 << (len(nums) - 1)):
		if operate(nums, ops) == val:
			return True
	return False

def conoperate(nums, ops):
	res = nums[0]
	op = 2 * (len(nums) - 2)
	for num in nums[1:]:
		chk = ops >> op
		if chk & 2:
			res = int(str(res) + str(num))
		else:
			res = (res * num) if chk & 1 else (res + num)
		op -= 2
	return res

def is_concatenateable(eq):
	val, nums = eq[0], eq[1]
	for ops in range(1 << (2 * (len(nums) - 1))):
		if ops % 4 == 3:
			continue
		if conoperate(nums, ops) == val:
			#print(f'{eq} - ops: {ops}')
			return True
	return False

def main():
	eqs = read()
	count = 0
	for eq in eqs:
		if is_possible(eq):
			count += eq[0]
	print(count)
	count = 0
	for eq in eqs:
		if is_concatenateable(eq):
			count += eq[0]
	print(count)

if __name__ == "__main__":
	main()
