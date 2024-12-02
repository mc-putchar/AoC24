def get_levels(file: str) -> list:
	levels = []
	with open(file, 'r') as f:
		text = f.read().splitlines()
	for line in text:
		level = [int(n) for n in line.split()]
		levels.append(level)
	return levels

def is_safe(level: list) -> bool:
	descending = level[0] > level[1]
	if descending:
		if not all(a>b and a - b < 4 for a,b in zip(level, level[1:])):
			return False
	else:
		if not all(a<b and b - a < 4 for a,b in zip(level, level[1:])):
			return False
	return True

def dampen(level: list) -> bool:
	for i in range(len(level)):
		dampened = level.copy()
		del (dampened[i])
		if is_safe(dampened):
			return True
	return False

def main():
	levels = get_levels('input')
	safe = [is_safe(level) for level in levels].count(True)
	print(safe)
	dampened_safe = [is_safe(level) or dampen(level) for level in levels].count(True)
	print(dampened_safe)

if __name__ == "__main__":
	main()
