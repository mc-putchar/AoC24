from collections import defaultdict

def load_input():
    ordering_rules = defaultdict(list)
    rules_loaded = False
    update_pages = []
    with open("input", "r") as f:
        for line in f:
            if line == "\n":
                rules_loaded = True
                continue
            if not rules_loaded:
                k, v = line.strip().split('|')
                ordering_rules[int(k)].append(int(v))
            else:
                update = [int(n) for n in line.strip().split(',')]
                update_pages.append(update)
    return ordering_rules, update_pages

def is_in_order(update, rules):
    for idx in range(len(update)):
        for prev in range(idx - 1, -1, -1):
            if update[prev] in rules[update[idx]]:
                return False
    return True

def order(update, rules):
    ordered = []
    for idx in range(len(update)):
        ins = len(ordered)
        for check in range(len(ordered)):
            if ordered[check] in rules[update[idx]]:
                ins = check
                break
        ordered.insert(ins, update[idx])
    return ordered[len(ordered) // 2]

def main():
    rules, pages = load_input()
    middle = 0
    unordered = []
    for update in pages:
        if is_in_order(update, rules):
            middle += update[len(update) // 2]
        else:
            unordered.append(update)
    print(middle)
    middle = 0
    for update in unordered:
        middle += order(update, rules)
    print(middle)

if __name__ == "__main__":
    main()
